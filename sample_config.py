#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging
from pyrogram import Client
import asyncio

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = "750714315"

    # Get from my.telegram.org
    APP_ID = int(3547531)

    # Get from my.telegram.org
    API_HASH = "03e1660b2bdd9ab6fd913fe49300fb00"

    # Generate a user session string - 会自动检查和生成
    TG_USER_SESSION = None  # 将在启动时自动设置

    # Database URI - 使用 SQLite
    DB_URI = "sqlite:///clonebot.db"

    @staticmethod
    async def generate_session_string_async():
        """异步生成用户会话字符串"""
        print("\n=== 生成用户会话字符串 ===")
        print("请输入您的 Telegram 账户信息：")
        
        try:
            # 创建临时客户端来生成会话字符串
            temp_client = Client(
                name="temp_session",
                api_id=Config.APP_ID,
                api_hash=Config.API_HASH,
                in_memory=True
            )
            
            # 启动客户端并获取会话字符串
            async with temp_client:
                session_string = await temp_client.export_session_string()
                print(f"\n✅ 会话字符串生成成功！")
                return session_string
                
        except Exception as e:
            print(f"❌ 生成会话字符串时出错: {e}")
            print("\n💡 解决建议:")
            print("1. 确保您的网络连接正常")
            print("2. 检查 APP_ID 和 API_HASH 是否正确")
            print("3. 尝试使用 VPN 或更换网络环境")
            print("4. 确保 Pyrogram 版本是最新的")
            return None
    
    @staticmethod
    def generate_session_string():
        """同步包装器"""
        return asyncio.run(Config.generate_session_string_async())
    
    @staticmethod
    async def validate_session_string_async(session_string):
        """异步验证会话字符串是否有效"""
        if not session_string or session_string == "Your_user_session_string_compatible_with_Pyrogram_v2":
            return False
            
        try:
            # 创建临时客户端测试会话字符串
            temp_client = Client(
                name="validate_session",
                session_string=session_string,
                api_id=Config.APP_ID,
                api_hash=Config.API_HASH,
                in_memory=True
            )
            
            # 尝试连接测试
            async with temp_client:
                await temp_client.get_me()
                return True
                
        except Exception:
            return False
    
    @staticmethod
    def validate_session_string(session_string):
        """同步包装器"""
        return asyncio.run(Config.validate_session_string_async(session_string))
    
    @staticmethod
    def load_or_generate_session():
        """加载或生成会话字符串"""
        session_file = "user_session.txt"
        
        # 检查是否存在保存的会话字符串
        if os.path.exists(session_file):
            try:
                with open(session_file, 'r', encoding='utf-8') as f:
                    saved_session = f.read().strip()
                
                print("🔍 检查已保存的会话字符串...")
                if Config.validate_session_string(saved_session):
                    print("✅ 会话字符串有效，使用已保存的会话")
                    Config.TG_USER_SESSION = saved_session
                    return saved_session
                else:
                    print("❌ 已保存的会话字符串无效或已过期")
            except Exception as e:
                print(f"❌ 读取会话文件时出错: {e}")
        
        # 生成新的会话字符串
        print("\n🔄 需要生成新的会话字符串...")
        new_session = Config.generate_session_string()
        
        if new_session:
            # 保存会话字符串到文件
            try:
                with open(session_file, 'w', encoding='utf-8') as f:
                    f.write(new_session)
                print(f"💾 会话字符串已保存到 {session_file}")
                Config.TG_USER_SESSION = new_session
                return new_session
            except Exception as e:
                print(f"❌ 保存会话字符串时出错: {e}")
                Config.TG_USER_SESSION = new_session
                return new_session
        else:
            print("❌ 无法生成会话字符串")
            print("\n🔧 手动生成会话字符串的方法:")
            print("1. 运行以下 Python 代码:")
            print("```python")
            print("from pyrogram import Client")
            print(f"app = Client('my_account', api_id={Config.APP_ID}, api_hash='{Config.API_HASH}')")
            print("with app:")
            print("    print(app.export_session_string())")
            print("```")
            print("2. 将生成的会话字符串保存到 user_session.txt 文件中")
            exit(1)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# 兼容性别名
logger = LOGGER

# 在模块加载时自动检查和生成会话字符串
if Config.TG_USER_SESSION is None:
    print("🚀 正在初始化用户会话...")
    Config.load_or_generate_session()
