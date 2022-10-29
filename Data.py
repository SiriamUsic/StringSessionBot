from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton(" اضغط لبدا استخراج الكود", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="رجوع", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀", url="https://t.me/JAVA_tlethon"
            )
        ],
        [
            InlineKeyboardButton("طريقة الاستخدام", callback_data="help"),
            InlineKeyboardButton("معلومات", callback_data="about"),
        ],
        [InlineKeyboardButton("مبرمج البوت", url="https://t.me/Salah_officiall")],
    ]

    START = """
اهلا {}
اهلا بك في {}
⚡¦يـمكنك استـخـراج الـتـالـي
♻️¦تيرمـكـس تليثون للحسـابـات🏂
♻️¦تيرمـكـس تليثون للبوتــات🤖
🎧¦بايـروجـرام مـيوزك للحسابات🙋🏼‍♂️
🗽¦بايـروجـرام مـيوزك احدث اصدار🎊
🎧¦بايـروجـرام مـيوزك للبوتات🤖
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت
ʙʏ @JAVA_tlethon
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

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @JAVA_tlethon 

السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/JAVA_tlethon)
المكاتب : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغه : [ᴘʏᴛʜᴏɴ](www.python.org)
المالك : @Salah_officiall 
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
💥 A ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ
ᴏғ ♻️pokemon 🔥
━━━━━━━━━━━━━━━━━
ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ғᴏʀ ᴛɢ...
┏━━━━━━━━━━━━━━━━━┓
┣★ المطور [pokemon](https://t.me/Salah_officiall)
┣★ للعظمة  [ʜᴇᴀʀᴛ ❤️](https://t.me/JAVA_tlethon)
┣★ بار التيم [مساعده](https://t.me/Supports)
┣★ المطور [Cristen](https://t.me/Hk_MB)
┗━━━━━━━━━━━━━━━━━┛
💞 
لو عند اساله تعاله بف » TO » MY » [OWNER] @Salah_officiall 
   """
