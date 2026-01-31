# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
import re, os, time
id_pattern = re.compile(r'^.\d+$') 
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27226524")
    API_HASH  = os.environ.get("API_HASH", "a14c9cd4629fde6b4d9b8c77df00fb00")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8031734602:AAGKgEPYhwgVOSDXk2uq4PHIZUWww6MZaYM")
    PORT = os.environ.get("PORT", "8980")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "RexBots")     
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://ANI_OTAKU:ANI_OTAKU@cluster0.t3frstc.mongodb.net/?appName=Cluster0")
 
    # other configs
    ADMIN_URL = "https://t.me/ITSANIMEN"
    DUMP_CHANNEL = os.environ.get("DUMP_CHANNEL", "-1002983564230")
    DUMP = True
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://ibb.co/wZCjM8JZ")
    LEADERBOARD_PIC = os.environ.get("LEADERBOARD_PIC", "https://ibb.co/5gVJD0HQ")
    OWNER_ID = int(os.environ.get("OWNER_ID", "6213241700"))
    SUPPORT_CHAT = int(os.environ.get("SUPPORT_CHAT", "-1003435722587"))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003548938800"))
    FSUB_PIC = os.environ.get("FSUB_PIC", "https://ibb.co/qLJPb3M5")
    VERIFY_PIC=os.environ.get("VERIFY_PIC", "")
    HOME_PIC=os.environ.get("HOME_PIC", "")
    HELP_PIC=os.environ.get("HELP_PIC", "")
    PREMIUM_PIC=os.environ.get("PREMIUM_PIC", "")
    ABOUT_PIC=os.environ.get("ABOUT_PIC", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ANIME_uploader_ON_bot")
    LEADERBOARD_DELETE_TIMER = 30
    # wes response configuration     
   # WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))
    
    #========================================================================================   
    START_TXT = """<b>ʜᴇʏ! {mention}  

» ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ! \n<b>➤ ᴘᴜʀᴘᴏꜱᴇ ᴏꜰ ᴛʜᴇ ʙᴏᴛ:</b>\nᴛʜɪꜱ ʙᴏᴛ ᴍᴀᴋᴇꜱ ʀᴇɴᴀᴍɪɴɢ ᴀɴɪᴍᴇ ᴀɴᴅ ꜱᴇʀɪᴇꜱ ꜰɪʟᴇꜱ ᴇᴀꜱʏ ᴀɴᴅ \nꜱᴛʀᴇꜱꜱ-ꜰʀᴇᴇ.\n\n<b>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ :</b> <a href="https://t.me/ITSANIMEN">彡 ΔNI_OTΔKU 彡</a>\n──────────────────</b>"""
    
    FILE_NAME_TXT = """<b>» <u>sᴇᴛᴜᴘ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ғᴏʀᴍᴀᴛ</u></b>

<b>ᴠᴀʀɪᴀʙʟᴇꜱ :</b>
➲ ᴇᴘɪꜱᴏᴅᴇ - ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴇᴘɪꜱᴏᴅᴇ ɴᴜᴍʙᴇʀ
➲ ǫᴜᴀʟɪᴛʏ - ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ǫᴜᴀʟɪᴛʏ

<b>‣ ꜰᴏʀ ᴇx:- </b> <code> /autorename Your Anime Name Here [SSeason] [EPEpisode] [Quality] [Audio] @ANI_MARK_NET </code>

<b>‣ /Autorename: ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ꜰɪʟᴇꜱ ʙʏ ɪɴᴄʟᴜᴅɪɴɢ 'ᴇᴘɪꜱᴏᴅᴇ' ᴀɴᴅ 'ǫᴜᴀʟɪᴛʏ' ᴠᴀʀɪᴀʙʟᴇꜱ ɪɴ ʏᴏᴜʀ ᴛᴇxᴛ, ᴛᴏ ᴇxᴛʀᴀᴄᴛ ᴇᴘɪꜱᴏᴅᴇ ᴀɴᴅ ǫᴜᴀʟɪᴛʏ ᴘʀᴇꜱᴇɴᴛ ɪɴ ᴛʜᴇ ᴏʀɪɢɪɴᴀʟ ꜰɪʟᴇɴᴀᴍᴇ. """
    
    ABOUT_TXT = f"""<b><blockquote expandable>❍ <u>ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴏғ :</u> : <b><i><a href="https://t.me/ANIME_uploader_ON_bot">𝐀𝐮𝐭𝐨𝐑𝐞𝐧𝐚𝐦𝐞 𝐁𝐎𝐓</a></i></b>
❍ ᴅᴇᴠᴇʟᴏᴩᴇʀ : <a href="https://t.me/Akuma_Rei_Kami">Akuma Rei (悪魔霊)</a>
❍ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
❍ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
❍ ʜᴏꜱᴛᴇᴅ ᴏɴ : <a href="https://t.me/BotifyX_Pro">ᴠᴘs</a>
❍ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/BotifyX_Pro">𝗕𝗼𝘁𝗶𝗳𝘆𝗫_𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹</a></b>

<b>➻ ꜰᴇᴀᴛᴜʀᴇꜱ :</b>
➲ ɪ ᴄᴀɴ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ʙᴀꜱᴇᴅ ᴏɴ ᴄᴜꜱᴛᴏᴍ ꜱᴇᴛᴛɪɴɢꜱ.
➲ ɪ ꜱᴜᴘᴘᴏʀᴛ ꜱᴇᴀꜱᴏɴ, ᴇᴘɪꜱᴏᴅᴇ, ǫᴜᴀʟɪᴛʏ, ᴀɴᴅ ᴏᴛʜᴇʀ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴀᴜᴛᴏ-ᴇxᴛʀᴀᴄᴛɪᴏɴ.
<b>➲ ꜰᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴄʀᴇᴀᴛᴏʀ</blockquote></b>"""

    
    THUMBNAIL_TXT = """<b><u>» ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ</u></b>
    
➲ /start: ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜱᴇᴛ ɪᴛ ᴀꜱ ᴀ ᴛʜᴜᴍʙɴᴀɪʟ..
➲ /del_thumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴏʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ.
➲ /view_thumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

ɴᴏᴛᴇ: ɪꜰ ɴᴏ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ɪɴ ʙᴏᴛ ᴛʜᴇɴ, ɪᴛ ᴡɪʟʟ ᴜꜱᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ᴛʜᴇ ᴏʀɪɢɪɴɪᴀʟ ꜰɪʟᴇ ᴛᴏ ꜱᴇᴛ ɪɴ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ"""

    CAPTION_TXT = """<b><u>» ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ</u></b>
    
<b>ᴠᴀʀɪᴀʙʟᴇꜱ :</b>         
ꜱɪᴢᴇ: {ꜰɪʟᴇꜱɪᴢᴇ}
ᴅᴜʀᴀᴛɪᴏɴ: {duration}
ꜰɪʟᴇɴᴀᴍᴇ: {ꜰɪʟᴇɴᴀᴍᴇ}

➲ /set_caption: ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
➲ /see_caption: ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
➲ /del_caption: ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.

» ꜰᴏʀ ᴇx:- /set_caption ꜰɪʟᴇ ɴᴀᴍᴇ: {ꜰɪʟᴇɴᴀᴍᴇ}"""

    PROGRESS_BAR = """\n
<b>Size</b> : {1} | {2}
<b>Done</b> : {0}%
<b>Speed</b> : {3}/s
<b>ETA</b> : {4} """
    
    
    DONATE_TXT = """<b><blockquote>ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ ᴀɴᴅ ᴇɴJᴏʏ ᴇxᴄʟᴜsɪᴠᴇ ғᴇᴀᴛᴜʀᴇs:</blockquote>
○ ᴜɴʟɪᴍɪᴛᴇᴅ Rᴇɴᴀᴍɪɴɢ.
○ ɴᴏ ᴀᴅꜱ.
○ ᴇᴀʀʟʏ Aᴄᴄᴇss.
○ ᴍᴏʀᴇ ᴘʀɪᴏʀɪᴛʏ

• ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.

➲ ғɪʀsᴛ sᴛᴇᴘ : ᴘᴀʏ ᴛʜᴇ ᴀᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ ᴘʟᴀɴ ᴛᴏ ᴛʜᴇ ᴜᴘɪ ɪᴅ ᴏʀ Qʀ.
➲ secoɴᴅ sᴛᴇᴘ : ᴛᴀᴋᴇ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ ᴀɴᴅ sʜᴀʀᴇ ɪᴛ ᴅɪʀᴇᴄᴛʟʏ ʜᴇʀᴇ: @Akuma_Rei_Kami & @ITSANIMEN
➲ ᴀʟᴛᴇʀɴᴀᴛɪᴠᴇ sᴛᴇᴘ : ᴏʀ ᴜᴘʟᴏᴀᴅ ᴛʜᴇ sᴄʀᴇᴇɴsʜᴏᴛ ʜᴇʀᴇ ᴀɴᴅ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛʜᴇ /bought ᴄᴏᴍᴍᴀɴᴅ. [ᴍᴀʏ ɴᴏᴛ ᴡᴏʀᴋ ᴘʀᴏᴘᴇʀʟʏ]

Yᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ ᴡɪʟʟ ʙᴇ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴀғᴛᴇʀ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ</b>
"""

    
    HELP_TXT = """<b>ʜᴇʀᴇ ɪꜱ ʜᴇʟᴘ ᴍᴇɴᴜ ɪᴍᴘᴏʀᴛᴀɴᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:

ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs🫧

ʀᴇɴᴀᴍᴇ ʙᴏᴛ ɪꜱ ᴀ ʜᴀɴᴅʏ ᴛᴏᴏʟ ᴛʜᴀᴛ ʜᴇʟᴘꜱ ʏᴏᴜ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ ᴇꜰꜰᴏʀᴛʟᴇꜱꜱʟʏ.

➲ /autorename: ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ.
➲ /metadata: ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴛᴜʀɴ ᴏɴ ᴏғғ ᴍᴇᴛᴀᴅᴀᴛᴀ.
➲ /help: ɢᴇᴛ ǫᴜɪᴄᴋ ᴀꜱꜱɪꜱᴛᴀɴᴄᴇ.</b>"""

    VERIFY_TEXT = """<b>ʜᴇʏ {mention},

‼️ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴠᴇʀɪғɪᴇᴅ ᴛᴏᴅᴀʏ ‼️
⚠️ Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ ғɪʀsᴛ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴀᴄᴄᴇss ᴏғ ʀᴇɴᴀᴍɪɴɢ ᴛʜᴇ ғɪʟᴇs
ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ ᴀɴᴅ ᴇɴJᴏʏ ᴇxᴄʟᴜsɪᴠᴇ ғᴇᴀᴛᴜʀᴇs:
• ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.

Cʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴠᴇʀɪғʏ.
⏰ Vᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴠᴀʟɪᴅ ғᴏʀ 24 ʜᴏᴜʀs
Tᴏᴋᴇɴ ᴇxᴘɪʀᴇs ɪɴ 24 ʜᴏᴜʀs...
   </b> """
#================================================================================


# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄

# --


