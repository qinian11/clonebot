from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


home_button = [
    [
        InlineKeyboardButton("🌏 源聊天", "source_btn"),
        InlineKeyboardButton("⬇️  起始ID", "from_btn"),
        InlineKeyboardButton("❓ 帮助", url="https://bit.ly/3z2jquF")
    ],
    [
        InlineKeyboardButton("🎯 目标聊天", "target_btn"),
        InlineKeyboardButton("⬆️  结束ID", "up_to_btn"),
        InlineKeyboardButton("文件类型  ➡", "types_btn")
    ],
    [
        InlineKeyboardButton("延迟发送", "delay_btn"),
        InlineKeyboardButton("保留标题", "caption_btn"),
        InlineKeyboardButton("文件名标题", "f_caption_btn")
    ],
    [
        InlineKeyboardButton("🔎️  查看配置", "view_btn"),
        InlineKeyboardButton("✍️ 自定义标题", "cust_captn_btn"),
        InlineKeyboardButton("❌  关闭", "close_btn")
    ],
    [
        InlineKeyboardButton("🗑  重置", "rst_btn"),
        InlineKeyboardButton("🔄  重启", "restart_btn")
    ],
    [
        InlineKeyboardButton("🚦 开始克隆消息 🚦", "clone_btn")
    ]
]


start_button = [
    [
        InlineKeyboardButton("🏅 GitHub 🏅", url="github.com/m4mallu/clonebot"),
        InlineKeyboardButton("⚙️ 设置 ⚙", "start_btn")
    ]
]


types_button = [
    [
        InlineKeyboardButton("文档 ✅", "docs_yes_btn"),
        InlineKeyboardButton("视频 ✅", "video_yes_btn"),
        InlineKeyboardButton("音频 ✅", "audio_yes_btn")
    ],
    [
        InlineKeyboardButton("图片 ✅", "photo_yes_btn"),
        InlineKeyboardButton("语音 ✅", "voice_yes_btn"),
        InlineKeyboardButton("文本 ✅", "text_yes_btn")
    ],
    [
        InlineKeyboardButton("⚙️ 查看", "view_types"),
        InlineKeyboardButton("⬅️ 返回", "start_btn")
    ]
]


stop_button = [
    [
        InlineKeyboardButton("🚫 停止 🚫", "stop_clone")
    ]
]


finished_button = [
    [
        InlineKeyboardButton("主页", "start_btn"),
        InlineKeyboardButton("关闭", "close_btn")
    ]
]


close_button = [
    [
        InlineKeyboardButton("删除", "close_btn"),
        InlineKeyboardButton("关闭", "clear_btn")
    ]
]


terminate_btn = [
    [
        InlineKeyboardButton("🧸 更新", url="https://github.com/m4mallu/clonebot"),
        InlineKeyboardButton("❓ 使用说明", url="https://bit.ly/3z2jquF")
    ],
    [
        InlineKeyboardButton("🚫 终止", "terminate_btn"),
        InlineKeyboardButton("🏠 主页", "start_btn")
    ]
]


indexing_skip_button = [
        [
            InlineKeyboardButton("🕹 跳过", "index_skip_btn")
        ]
    ]


purging_skip_button = [
        [
            InlineKeyboardButton("🕹 跳过", "purge_skip_btn")
        ]
    ]


purge_button = [
    [
        InlineKeyboardButton("不清除", "purge_no_btn"),
        InlineKeyboardButton("清除 👍", "purge_yes_btn")
    ]
]

caption_cnf_button = [
    [
        InlineKeyboardButton("是 ✅", "capt_cnf_yes_btn"),
        InlineKeyboardButton("否 ❌", "capt_cnf_no_btn")
    ]
]

# ... existing code ...
