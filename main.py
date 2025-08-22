import asyncio
from bot import Bot

# 为 Windows 设置事件循环策略（解决 Python 3.10+ 兼容性问题）
if hasattr(asyncio, 'WindowsSelectorEventLoopPolicy'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

Bot().run()
