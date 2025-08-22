import threading
from config import Config
from sqlalchemy import create_engine
from sqlalchemy import Column, Boolean, Numeric
# 新版 SQLAlchemy 2.0+ 的导入方式
try:
    from sqlalchemy.orm import declarative_base
except ImportError:
    from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

clone_cancel_key = {}       # Clone cancel status key
clone_btn_count = {}        # Clone button single click actuator key
index_skip_key = {}         # Skip indexing function key
purge_skip_key = {}         # Purge function key

custom_caption = {}         # Custom caption key
master_index = []           # Unique id index of cloning medias (including target chat)
file_types = ["document", "video", "audio", "voice", "photo", "text"]

# 先定义 BASE
BASE = declarative_base()

class Clonebot(BASE):
    __tablename__ = "clonebot"
    id = Column(Numeric, primary_key=True)
    s_chat = Column(Numeric)
    d_chat = Column(Numeric)
    from_id = Column(Numeric)
    to_id = Column(Numeric)
    s_chat_msg_id = Column(Numeric)
    d_chat_msg_id = Column(Numeric)
    from_msg_id = Column(Numeric)
    to_msg_id = Column(Numeric)
    delayed_clone = Column(Boolean)
    caption = Column(Boolean)
    file_caption = Column(Boolean)
    last_msg_id = Column(Numeric)

    def __init__(self, id, s_chat, s_chat_msg_id, d_chat, d_chat_msg_id, from_id, from_msg_id, to_id, to_msg_id,
                 delayed_clone, caption, file_caption, last_msg_id):
        self.id = id
        self.s_chat = s_chat
        self.d_chat = d_chat
        self.s_chat_msg_id = s_chat_msg_id
        self.d_chat_msg_id = d_chat_msg_id
        self.from_id = from_id
        self.from_msg_id = from_msg_id
        self.to_id = to_id
        self.to_msg_id = to_msg_id
        self.delayed_clone = delayed_clone
        self.caption = caption
        self.file_caption = file_caption
        self.last_msg_id = last_msg_id

def start() -> scoped_session:
    # 移除过时的 client_encoding 参数
    engine = create_engine(Config.DB_URI)
    
    # 创建所有表
    try:
        BASE.metadata.create_all(engine)
        print("✅ 数据库表创建成功")
    except Exception as e:
        print(f"⚠️ 数据库表创建警告: {e}")
    
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

# 初始化数据库连接
SESSION = start()
INSERTION_LOCK = threading.RLock()

async def add_user(id):
    with INSERTION_LOCK:
        try:
            msg = SESSION.query(Clonebot).get(id)
            if not msg:
                usr = Clonebot(id, 0, 0, 0, 0, 0, 0, 0, 0, False, True, False, 0)
                SESSION.add(usr)
                SESSION.commit()
        except Exception as e:
            print(f"❌ 添加用户时出错: {e}")
            SESSION.rollback()

async def source_force_reply(id, s_chat_msg_id):
    with INSERTION_LOCK:
        try:
            SESSION.query(Clonebot).filter(Clonebot.id == id).update({'s_chat_msg_id': s_chat_msg_id})
            SESSION.commit()
        except Exception as e:
            print(f"❌ 更新源强制回复时出错: {e}")
            SESSION.rollback()

async def source_cnf_db(id, value):
    with INSERTION_LOCK:
        try:
            SESSION.query(Clonebot).filter(Clonebot.id == id).update({'s_chat': value, 'last_msg_id': 0})
            SESSION.commit()
        except Exception as e:
            print(f"❌ 更新源配置时出错: {e}")
            SESSION.rollback()

async def target_force_reply(id, d_chat_msg_id):
    with INSERTION_LOCK:
        try:
            SESSION.query(Clonebot).filter(Clonebot.id == id).update({'d_chat_msg_id': d_chat_msg_id})
            SESSION.commit()
        except Exception as e:
            print(f"❌ 更新目标强制回复时出错: {e}")
            SESSION.rollback()

async def target_cnf_db(id, value):
    with INSERTION_LOCK:
        try:
            SESSION.query(Clonebot).filter(Clonebot.id == id).update({'d_chat': value})
            SESSION.commit()
        except Exception as e:
            print(f"❌ 更新目标配置时出错: {e}")
            SESSION.rollback()

async def from_msg_id_force_reply(id, from_msg_id):
    with INSERTION_LOCK:
        try:
            SESSION.query(Clonebot).filter(Clonebot.id == id).update({'from_msg_id': from_msg_id})
            SESSION.commit()
        except Exception as e:
            print(f"❌ 更新起始消息ID时出错: {e}")
            SESSION.rollback()

async def from_msg_id_cnf_db(id, value):
    with INSERTION_LOCK:
        try:
            SESSION.query(Clonebot).filter(Clonebot.id == id).update({'from_id': value})
            SESSION.commit()
        except Exception as e:
            print(f"❌ 更新起始消息配置时出错: {e}")
            SESSION.rollback()

async def to_msg_id_force_reply(id, to_id):
    with INSERTION_LOCK:
        try:
            SESSION.query(Clonebot).filter(Clonebot.id == id).update({'to_msg_id': to_id})
            SESSION.commit()
        except Exception as e:
            print(f"❌ 更新结束消息ID时出错: {e}")
            SESSION.rollback()

async def to_msg_id_cnf_db(id, value):
    with INSERTION_LOCK:
        try:
            SESSION.query(Clonebot).filter(Clonebot.id == id).update({'to_id': value})
            SESSION.commit()
        except Exception as e:
            print(f"❌ 更新结束消息配置时出错: {e}")
            SESSION.rollback()

async def query_msg(id):
    try:
        return SESSION.query(Clonebot).get(id)
    except Exception as e:
        print(f"❌ 查询消息时出错: {e}")
        return None

async def del_from_to_ids(id):
    with INSERTION_LOCK:
        try:
            SESSION.query(Clonebot).filter(Clonebot.id == id).update({'from_id': 0, 'to_id': 0})
            SESSION.commit()
        except Exception as e:
            print(f"❌ 删除起始结束ID时出错: {e}")
            SESSION.rollback()

async def change_delay(id):
    with INSERTION_LOCK:
        try:
            msg = SESSION.query(Clonebot).get(id)
            if msg:
                if msg.delayed_clone:
                    SESSION.query(Clonebot).filter(Clonebot.id == id).update({'delayed_clone': False})
                else:
                    SESSION.query(Clonebot).filter(Clonebot.id == id).update({'delayed_clone': True})
                SESSION.commit()
        except Exception as e:
            print(f"❌ 更改延迟设置时出错: {e}")
            SESSION.rollback()

async def opt_caption(id):
    with INSERTION_LOCK:
        try:
            msg = SESSION.query(Clonebot).get(id)
            if msg:
                if msg.caption:
                    SESSION.query(Clonebot).filter(Clonebot.id == id).update({'caption': False})
                else:
                    SESSION.query(Clonebot).filter(Clonebot.id == id).update({'caption': True})
                SESSION.commit()
        except Exception as e:
            print(f"❌ 更改标题设置时出错: {e}")
            SESSION.rollback()

async def opt_FN_caption(id):
    with INSERTION_LOCK:
        try:
            msg = SESSION.query(Clonebot).get(id)
            if msg:
                if msg.file_caption:
                    SESSION.query(Clonebot).filter(Clonebot.id == id).update({'file_caption': False})
                else:
                    SESSION.query(Clonebot).filter(Clonebot.id == id).update({'file_caption': True})
                SESSION.commit()
        except Exception as e:
            print(f"❌ 更改文件标题设置时出错: {e}")
            SESSION.rollback()

async def msg_id_limit(id, value):
    with INSERTION_LOCK:
        try:
            SESSION.query(Clonebot).filter(Clonebot.id == id).update({'last_msg_id': value})
            SESSION.commit()
        except Exception as e:
            print(f"❌ 更新消息ID限制时出错: {e}")
            SESSION.rollback()

async def reset_all(id):
    with INSERTION_LOCK:
        try:
            SESSION.query(Clonebot).filter(Clonebot.id == id).update(
                {
                    's_chat': 0, 'd_chat': 0, 'from_id': 0, 'to_id': 0, 's_chat_msg_id': 0, 'd_chat_msg_id': 0,
                    'from_msg_id': 0, 'to_msg_id': 0, 'delayed_clone': False, 'caption': True, 'file_caption': False,
                    'last_msg_id': 0
                }
            )
            SESSION.commit()
        except Exception as e:
            print(f"❌ 重置所有设置时出错: {e}")
            SESSION.rollback()
