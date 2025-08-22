# ----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
class Presets(object):
    START_TEXT = "你好... {}\n我可以将任何聊天中的媒体文件克隆到你的个人聊天中！" \
                 "点击设置来配置我。如果你喜欢我，" \
                 "请在我的 GitHub 仓库中给个星标。谢谢！"
    WELCOME_TEXT = "⭑⭑★✪ 查看帮助获取更多信息: ✪★⭑⭑"
    MESSAGE_COUNT = """
╭──────⌈ 📥 克隆中 ⌋──────╮<code>
├ 消息ID - {}
├ 传输数 - {}
├ 进度 - {} %
├ 用时 - {} {}
├ 开始时间 - {}
├ 最后更新 - {}</code>
├  🔰 <a href='t.me/RMProjects'><b>@RMProjects</b></a> || 🏅 <a href='https://github.com/m4mallu/clonebot-ui'><b>@Github</b></a>
╰──────⌈ 💢 克隆机器人 ⌋─────╯"""
    DUPLICATE_INDEX = """
╭──────⌈ ⚠️ 跳过中 ⌋──────╮<code>
├ 消息ID - {}
├ 总数 - {}</code>
╰──────⌈ 💢 克隆机器人 ⌋──────╯"""
    INDEXING_MSG = """
╭─────⌈ ⚠️ 索引中 ⌋─────╮<code>
├ 正在索引目标聊天
├
├ 当前消息ID - {}
├ 最后消息ID - {}
├ 重复文件 - {}</code>
╰─────⌈ 💢 克隆机器人 ⌋─────╯
\xad             \xad"""
    INFO_CHAT_TYPES = """
你可以输入以下类型:

ID           : 123456789 (-100 不需要)
邀请链接      : https://t.me/joinchat/
公开链接      : https://t.me/python
用户名        : @python
    """
    SELECTED_TYPE = """
你已选择:
----------------------------
{} 文档
{} 音频
{} 视频
{} 图片
{} 语音
{} 文本
    """
    VIEW_CONF = """
源聊天ID : {}
目标聊天ID : {}
起始消息ID : {} | 结束消息ID : {}
延迟发送 : {} | 保留标题 : {}"""
    FILE_TYPES = ["document", "video", "audio", "voice", "photo", "text"]
    COPIED_MESSAGES = "<b><a href='https://github.com/m4mallu/clonebot'>媒体已复制</a></b>"
    IN_CORRECT_PERMISSIONS_MESSAGE_DEST_POSTING = "访问被拒绝\n\n用户不是管理员或在指定聊天中没有" \
                                                  "发布权限"
    USER_ABSENT_MSG = "会话用户不在指定的目标聊天中"
    CANCEL_CLONE = "正在停止进程... 请稍等 🕚"
    CANCELLED_MSG = "⚠      用户已取消克隆      ⚠"
    RESTART_MSG = "✅ 机器人已成功重启 ✅"
    RESTART_MSG_ERROR = "❌ 您没有权限 ❌"
    CAPTION_ERROR = """
🔊 自定义标题:
-------------------------------
⚠️ 在我的数据库中发现了自定义标题。请在使用此功能前在CC中清除它。"""
    CUSTOM_CAPTION_MSG_CLR = """
🔊 自定义标题:
-------------------------------
自定义标题消息已成功清除 ✅"""
    TEXT_UPDATE_MSG = "<code>您想将此文本设置为自定义标题吗？</code>"
    CUSTOM_CAPTION_MSG = """
🔊 自定义标题:
-------------------------------
向机器人聊天发送任何文本并按照说明设置自定义标题。"""
    CUSTOM_CAPTION_CNF = """
🔊 自定义标题:
-------------------------------
自定义标题消息已成功设置 ✅"""
    INITIAL_MESSAGE_TEXT = "🔎  正在初始化克隆  🔎"
    WAIT_MSG = "♻️ 处理中... 请稍等 "
    SOURCE_CNF = """
聊天名称: {}
聊天ID: <code> {}</code>
聊天类型: {}
聊天用户名: {}
位置: {}
成员数: {}
\xad                                                              \xad
源聊天已保存  ✅
                     """
    DEST_CNF = """
聊天名称: {}
聊天ID: <code> {}</code>
聊天类型: {}
聊天用户名: {}
位置: {}
成员数: {}
\xad                                                              \xad
目标聊天已保存  ✅
               """
    SESSION_START_INFO = """
用户会话已启动:

日期     :  {}
时间    :  {}

用户会话已在您的账户中启动，如果您知道这一点，请保持
此机器人不被屏蔽，您可以忽略此消息。如果您感觉
有问题，请终止此会话并屏蔽此机器人以避免
再次使用您的会话。当 Heroku 免费容器重启时
您可能会再次看到此消息。
    """
    NOT_CONFIGURED = "源聊天和目标聊天未配置 ⚠"
    NOT_AUTH_TEXT = "您没有权限  ⚠ "
    BOT_BLOCKED_MSG = "机器人被会话用户屏蔽！"
    NOT_CONFIGURED_CLONE = "未找到聊天配置 ⚠\n\n在克隆之前请配置源聊天和目标聊天 🤷"
    FINISHED_TEXT = "克隆已成功完成  ✅"
    TERMINATED_MSG = "🚫 机器人已终止 🚫\n感觉有问题？屏蔽此机器人以避免再次使用您的会话！"
    COPY_ERROR = "出现错误！\n\n系统中止了复制\n请检查所有用户权限。"
    INVALID_CHAT_ID = "<u>发现无效的聊天参数</u>\n\n原因:\n1. 会话用户不在私人聊天中\n" \
                      "2. 对于公开聊天，请使用'@用户名'\n或链接而不是'id'"
    ASK_SOURCE = "请提供源聊天信息:\n您有30秒时间完成此操作.."
    ASK_DESTINATION = "请提供目标聊天信息:\n您有30秒时间完成此操作.."
    ASK_START_MSG_ID = "请提供起始消息ID:\n您有30秒时间完成此操作.."
    ASK_END_MSG_ID = "请提供结束消息ID\n您有30秒时间完成此操作.."
    CHAT_DUPLICATED_MSG = "源聊天和目标聊天ID不能相同 "
    FROM_MSG_ID_CNF = "起始消息ID:👉 <code>{}</code> 👈 已保存  ✅"
    END_MSG_ID_CNF = "结束消息ID:👉 <code>{}</code> 👈 已保存  ✅"
    INVALID_MSG_ID = "消息ID应该是整数 ❗️"
    INVALID_REPLY_MSG = "无效的回复消息 ❗️"
    CNF_SOURCE_FIRST = "请先配置源聊天  ❗️"
    DELAY_OFF = "延迟克隆 : 已停用 🚫"
    DELAY_ON = "延迟克隆 : 已激活 [10秒] ✅"
    BLANK = "➖➖➖➖➖➖➖➖➖➖➖➖➖"
    BLOCK = "进度显示失败 :👉 帮助"
    CAPTION_ON = "文件标题 : 已激活 ✅"
    CAPTION_OFF = "文件标题 : 已停用 🚫"
    FN_AS_CAPT_ON = "文件名作为标题 : 已激活 ✅"
    FN_AS_CAPT_OFF = "文件名作为标题 : 已停用 🚫"
    NOT_REQUIRED = "此字段不是必填项  ⚠"
    RST_MSG = "重置为机器人默认设置 .. 已确认 ✅"
    TEST_MSG = "测试消息"
    OVER_FLOW = "超出最大限制！\n请检查允许的限制，重试！"
    SELECT_TYPE = "👉 点击将切换选择\n默认情况下全部选中！"
    CLONE_REPORT_CAPTION = "<b>克隆报告</b>"
    PURGE_PROMPT = "👉 <b>{}</b>  👈 <i>在您的目标聊天中发现重复文件。您现在想要清除它吗？</i>"
    PROCESSING_PURGE = "<b>🔷当前@: {}        🔷结束@: {}</b>\n\n<i>处理中.. 请稍等</i>"
    TARGET_CFG_LOAD_MSG = "<b><u>已导入</u>  ✅</b>\n\n<code>在我的数据库中找到了给定目标聊天的索引。" \
                          "它已加载到我的内存中。</code>\n\n<b><i>继续克隆..</i></b>"
    CLONE_REPORT = """
🔰 <b>克隆报告</b> 🔰

完成时间 : <b>{}</b>

源聊天 : <code>{}</code>
目标聊天  : <code>{}</code>

起始ID - {}
结束ID   - {}

🕐 延迟        - {}
✍️ 标题        - {}
🏷 文件名标题   - {}

<b>已克隆文件</b>  - {}

📚 文档     - {}
🎞 视频     - {}
🔊 音频     - {}
📸 图片     - {}
🗣 语音     - {}
📝 文本     - {}
⚠️ 重复     - {}

<u><b>致谢:</u></b> https://github.com/m4mallu
"""
    GET_CHAT_ID_MSG = "<b>您已收到来自聊天的转发消息\nID为:</b>\n\n<code>{" \
                      "}</code>\n<b>消息ID: </b><code>{}</code>\n\n<i>点击上面的文本复制！</i> "
    CLONE_REPORT_INFO = "报告已在您的收藏夹中生成。感谢使用此机器人 🤝"
