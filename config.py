import os
from pyrogram.types import KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton,WebAppInfo,ReplyKeyboardMarkup

#get it from https://n1panel.com
SMM_API_KEY:str=os.environ.get("SMM_API_KEY","")
API_ID:int =(os.environ.get("API_ID",None))

API_HASH:str = os.environ.get("API_HASH", "")
BOT_TOKEN:str = os.environ.get("BOT_TOKEN", "")
UPDATE_CHNL:str = os.environ.get("UPDATE_CHNL", "jn_bots")
OWNER_USERNAME:str = os.environ.get("OWNER_USERNAME", "jn_dev")
SUPPORT_GRP:str = os.environ.get("SUPPORT_GRP", "jn_smm")
START_IMG:str = os.environ.get(
    "START_IMG", "https://graph.org/file/aa5ca1df3286cee4fd332.jpg"
)

MONGO_DB_URI:str = os.environ.get(
    "MONGO_DB_URI",
    "",
)
OWNER_ID:int=os.environ.get("OWNER_ID",None)
INR_IMG="https://graph.org/file/292716c32a3129a0e3f78.jpg"

# //config  here

start_img2="https://graph.org/file/dd831607fd46bc90863af.jpg"
photo="https://graph.org/file/da9eb86b4c4a07ce4fa16.jpg"

desposit_text=f"""

🖥 Dᴇᴘᴏsɪᴛ Pʟᴀɴs

⚡️ 𝟷 Rs: Nᴏ Vɪᴇᴡs Bᴏɴᴜs
⚡️𝟷𝟶 Rs: 1k Vɪᴇᴡs Bᴏɴᴜs
⚡️𝟹𝟶 Rs: 4k Vɪᴇᴡs Bᴏɴᴜs
⚡️𝟻𝟶 Rs: 7k Vɪᴇᴡs Bᴏɴᴜs
⚡️𝟷𝟶𝟶 Rs: 15k Vɪᴇᴡs Bᴏɴᴜs 
⚡️ 200 Rs: 35K Vɪᴇᴡs Bᴏɴᴜs
⚡️ 500 Rs: 80ᴋ Vɪᴇᴡs Bᴏɴᴜs
⚡️ 1000: Rs 200ᴋ Vɪᴇᴡs Bᴏɴᴜs

💙"""
buttons = InlineKeyboardMarkup([[InlineKeyboardButton("• ᴘᴀʏ ᴡɪᴛʜ ᴜᴘɪ •", callback_data='INR')
]])

main_button = ReplyKeyboardMarkup(
        [
            [KeyboardButton("🪪 ᴍʏ ᴘʀᴏꜰɪʟᴇ"), KeyboardButton("💸 ᴀᴅᴅ ꜰᴜɴᴅ")],
            [KeyboardButton("📦 ɴᴇᴡ ᴏʀᴅᴇʀ"), KeyboardButton("🔭 ᴛʀᴀᴄᴋ ᴏʀᴅᴇʀ")], 
            [ KeyboardButton("🎗️ 𝕊𝕦𝕡𝕡𝕠𝕣𝕥 🎗️", web_app=WebAppInfo(url="https://jnbots.netlify.app"))]
        ],
        resize_keyboard=True
    )
post_view_img="https://graph.org/file/2701c46f3a7e064f92a7e.jpg"

voteview_img="https://graph.org/file/4fbe6a2bd1ec64dc68aed.jpg"

telegram_member_img="https://graph.org/file/a74ecfa3669ca7f824775.jpg"

telegram_story_img="https://graph.org/file/2f358825c272eb409626c.jpg"

#  ig
ig_gram=InlineKeyboardMarkup([[InlineKeyboardButton("👍 ʟɪᴋᴇꜱ", callback_data='ig_like')],[InlineKeyboardButton("ꜱᴛᴏʀʏ ᴠɪᴇᴡꜱ", callback_data='ig_story_view')],[InlineKeyboardButton("👥 ꜰᴏʟʟᴏᴡᴇꜱ ",callback_data='ig_follow')
]
])
img_all="https://graph.org/file/941d3ff9691e712d5773a.jpg"


img_instagram="https://graph.org/file/e3e825b55ea134a75cf6b.jpg"

img_instagram_like="https://graph.org/file/fb8204988f9b2a7c17eb4.jpg"
img_instagram_story="https://graph.org/file/5726f30df9d8f77b3ba65.jpg"
img_instagram_follow="https://graph.org/file/2b654e64fa47bd077178a.jpg"



img_youtube="https://graph.org/file/9b5ccaf8e3271592aae2c.jpg"
img_youtube_sub="https://graph.org/file/9b5ccaf8e3271592aae2c.jpg"
img_youtube_views="https://graph.org/file/9b5ccaf8e3271592aae2c.jpg"
img_youtube_like="https://graph.org/file/9b5ccaf8e3271592aae2c.jpg"
img_youtube_watchtime="https://graph.org/file/9b5ccaf8e3271592aae2c.jpg"






img_telegram="https://graph.org/file/2f16d7375b35adc81cdf7.jpg"

button_telegram=InlineKeyboardMarkup([[InlineKeyboardButton("👀 ᴘᴏꜱᴛ ᴠɪᴇᴡ", callback_data='post_view'),
InlineKeyboardButton("📊 ᴘᴏʟʟ ᴠᴏᴛᴇꜱ ", callback_data='pollvotes')
],
[InlineKeyboardButton("🐳 ᴇᴍᴏᴊɪ ʀᴇᴀᴄᴛɪᴏɴꜱ ",callback_data='emoji_reaction')],[InlineKeyboardButton("🎎 ᴍᴇᴍʙᴇʀꜱ/ꜱᴜʙꜱᴄʀɪʙᴇʀꜱ ",callback_data='Member')
],
[InlineKeyboardButton("👁 ꜱᴛᴏʀʏ ᴠɪᴇᴡꜱ ", callback_data='story_view')
]
])

button_youtube=InlineKeyboardMarkup([[InlineKeyboardButton("❤️ ꜱᴜʙꜱᴄʀɪʙᴇʀꜱ ", callback_data='Subscribe_yt'),InlineKeyboardButton("💠 ᴡᴀᴛᴄʜᴛɪᴍᴇ ",callback_data='WatchTime_yt')
],
[InlineKeyboardButton("👍🏽 ʟɪᴋᴇ ", callback_data='Likes_yt'),InlineKeyboardButton("👀 ᴠɪᴇᴡ ",callback_data='Views_yt')
]
])

all_platform = ReplyKeyboardMarkup(
        [
            [KeyboardButton("🔵 ᴛᴇʟᴇɢʀᴀᴍ ⊛"), KeyboardButton("🔴 ʏᴏᴜᴛᴜʙᴇ ⊛")],
            [KeyboardButton("🟣 ɪɴꜱᴛᴀɢʀᴀᴍ  ✇"), KeyboardButton("🔭 ᴛʀᴀᴄᴋ ᴏʀᴅᴇʀ")],
            [ KeyboardButton("〄 ᴍᴀɪɴ ᴍᴇɴᴜ 〄")]
        ],
        resize_keyboard=True
    )
    # ################### config

DGB_IMG="https://www.12thblog.com/wp-content/uploads/2019/10/Mia-Khalifa-22.jpg"

deposit_IMG="https://graph.org/file/b95a5f04f293fe7900261.jpg"
