from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("🔥 اضغط لبدا استخراج الكود 🔥", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 رجوع", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "✨ ᦔꫀꪜ ρꪮ𝘬ꫀꪑꪮꪀ ✨", url="https://t.me/wjj_u"
            )
        ],
        [
            InlineKeyboardButton("🤔 طريقة الاستخدام 🤔", callback_data="help"),
            InlineKeyboardButton("🎪 معلومات 🎪", callback_data="about"),
        ],
        [InlineKeyboardButton("💌 قناة السورس 💌", url="https://t.me/cr_source")],
    ]

    START = """
هلو {}
اهلا بك في {}
⚡¦يـمكنك استـخـراج الـتـالـي
♻️¦تيرمـكـس تليثون للحسـابـات🏂
♻️¦تيرمـكـس تليثون للبوتــات🤖
🎧¦بايـروجـرام مـيوزك للحسابات🙋🏼‍♂️
🗽¦بايـروجـرام مـيوزك احدث اصدار🎊
🎧¦بايـروجـرام مـيوزك للبوتات🤖
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت
ʙʏ @cr_source ᴀɴᴅ @gro_up_1 
    """

    HELP = """
✨ **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs** ✨

/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ
/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/repo - ɢᴇᴛ ʀᴇᴘᴏ
/generate - sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
/restart - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
"""

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @cr_source 

السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/cr_source)
المكاتب : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغه : [ᴘʏᴛʜᴏɴ](www.python.org)
المالك : @wjj_u 
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
💥 A ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ
ᴏғ ♻️pokemon 🔥
━━━━━━━━━━━━━━━━━
ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ғᴏʀ ᴛɢ...
┏━━━━━━━━━━━━━━━━━┓
┣★ المطور [pokemon](https://t.me/wjj_u)
┣★ للعظمة  [ʜᴇᴀʀᴛ ❤️](https://t.me/cr_source)
┣★ بار التيم [رغي](https://t.me/gro_up_1)
┣★ المطورة [Cristen](https://t.me/dr_criss)
┣★ السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/cr_source)
┣★ بار السورس [c.r team](https://t.me/SORS0Coo)
┗━━━━━━━━━━━━━━━━━┛
💞 
لو عند اساله تعاله بف » TO » MY » [OWNER] @wjj_u 
   """
