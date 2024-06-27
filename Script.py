class script(object):
    START_TXT = """<b>Hello {},
My name is <a href=https://t.me/{}>{}</a>,I can provide the latest movies and series. Proudly made by @NotPiracy

🤖 𝗠𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝗲𝗱 𝗕𝘆 : <a href='https://t.me/OffPiracy'>𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿</a></b>"""

    HELP_TXT = """<b>Hey {}
Here is the help for my commands.

🤖 𝗠𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝗲𝗱 𝗕𝘆: <a href='https://t.me/OffPiracy'>𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿</a></b>"""

    ABOUT_TXT = """<b>✯ 𝗠𝘆 𝗡𝗮𝗺𝗲 : {}</b>
<b>✯ 𝗖𝗿𝗲𝗮𝘁𝗼𝗿: <a href=https://t.me/notPiracy>𝗢𝗪𝗡𝗘𝗥</a></b>
<b>✯ 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 : <a href=https://t.me/MidNightXMoviesV1>𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a></b>
<b>✯ 𝗕𝘂𝗶𝗹𝗱 𝗦𝘁𝗮𝘁𝘂𝘀 : ᴠ3.0.1</b>"""

    SOURCE_TXT = """
<b>𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗶𝘀 𝗼𝗽𝗲𝗻 𝗦𝗼𝘂𝗿𝗰𝗲 𝗣𝗿𝗼𝗷𝗲𝗰𝘁
𝗙𝗼𝗿 𝗮𝗰𝗰𝗲𝘀𝘀 𝘁𝗼 𝘁𝗵𝗲 𝘀𝗼𝘂𝗿𝗰𝗲 𝗰𝗼𝗱𝗲 𝗼𝗳 𝘁𝗵𝗶𝘀 𝗼𝗽𝗲𝗻-𝘀𝗼𝘂𝗿𝗰𝗲 𝗽𝗿𝗼𝗷𝗲𝗰𝘁, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗻𝗼𝘁𝗲 𝘁𝗵𝗮𝘁 @𝗡𝗼𝘁𝗣𝗶𝗿𝗮𝗰𝘆 𝗵𝗮𝗻𝗱𝗹𝗲𝘀 𝗶𝗻𝗾𝘂𝗶𝗿𝗶𝗲𝘀 𝗿𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 𝗶𝘁

  

  CUDNT_FND = """I ᴄᴏᴜʟᴅɴ'ᴛ find anything related to {}

If spelling is correct and not found,

First please check out @MidNightSearchV3Bot

If not found on @MidNightSearchV3Bot

Then DM your request on @MidnightMoviesRequestBot.

Did you mean any one of these?"""

   I_CUDNT = """Sorry no files were found for your request {} 😕

Check your spelling in Google and try again 😃

If spelling is correct and not found,

First please check out @MidNightSearchV3Bot

If not found on @MidNightSearchV3Bot

Then DM your request on @MidnightMoviesRequestBot.

Movie request format 👇

Example: Uncharted or Uncharted 2022 or Uncharted En

Series request format 👇

Example: Loki S01 or Loki S01E04 or Lucifer S03E24

🚯 Don't use ➠ ':(!,./)</b>
"""

I_CUD_NT = """I couldn't find any movie related to {}.
Please check the spelling on Google or IMDb..."""

MVE_NT_FND = """Movie not found in database..."""

TOP_ALRT_MSG = """Checking for movie in database..."""

MELCOW_ENG = """<b>Hello {} 😍, And Welcome To {} Group ❤️</b>"""


    SHORTLINK_INFO = """
<b>──────「<a href=https://t.me/MaviUpload> Hᴏᴡ ᴛᴏ Eᴀʀɴ Mᴏɴᴇʏ </a> 」──────

Yᴏᴜ ᴄᴀɴ Eᴀʀɴ Mᴏɴᴇʏ Fʀᴏᴍ Tʜɪs Bᴏᴛ Uɴᴛɪʟ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟɪᴠᴇ.

Wᴀɴᴛ ᴛᴏ Kɴᴏᴡ Hᴏᴡ? Fᴏʟʟᴏᴡ Tʜᴇsᴇ Sᴛᴇᴘs:-

sᴛᴇᴘ 𝟷 : ʏᴏᴜ ᴍᴜsᴛ ʜᴀᴠᴇ ᴀᴛʟᴇᴀsᴛ ᴏɴᴇ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴍɪɴɪᴍᴜᴍ 1𝟶𝟶 ᴍᴇᴍʙᴇʀs.

sᴛᴇᴘ 𝟸 : ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ Aɴʏ >Sʜᴏʀᴛᴇɴᴇʀ Wᴇʙsɪᴛᴇ</a>.

sᴛᴇᴘ 𝟹 : ꜰᴏʟʟᴏᴡ ᴛʜᴇsᴇ <a href=https://t.me/MaviUpload> ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ </a>Tᴏ ᴄᴏɴɴᴇᴄᴛ sʜᴏʀᴛᴇɴᴇʀ.

➣ Yᴏᴜ ᴄᴀɴ ᴄᴏɴɴᴇᴄᴛ ᴀs ᴍᴀɴʏ ɢʀᴏᴜᴘ ʏᴏᴜ ʜᴀᴠᴇ.

Any Doubts or Not Connecting? Contact Me </b>
"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 5 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ"""

    SELECT = """
MOVIES ➢ Sᴇʟᴇᴄᴛ "Lᴀɴɢᴜᴀɢᴇs"

SERIES ➢ Sᴇʟᴇᴄᴛ "Sᴇᴀsᴏɴs"

Tɪᴘ: Sᴇʟᴇᴄᴛ "Lᴀɴɢᴜᴀɢᴇs" ᴏʀ "Sᴇᴀsᴏɴs" Bᴜᴛᴛᴏɴ ᴀɴᴅ Cʟɪᴄᴋ "Sᴇɴᴅ Aʟʟ" Tᴏ ɢᴇᴛ Aʟʟ Fɪʟᴇ Lɪɴᴋs ɪɴ ᴀ Sɪɴɢʟᴇ ᴄʟɪᴄᴋ"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """ 
<b>══════════════════
🗂 {file_name}
═══════════════════ 
𝐒𝐔𝐁𝐒𝐂𝐑𝐈𝐁𝐄 𝐇𝐄𝐑𝐄 👇
╔══════════════════╗         
    <a href="https://t.me/MidNightXMoviesV1">🔱 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 🔱</a>
╚══════════════════╝</b>"""
    
    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
⏱️ Result Shown in: {remaining_seconds} <i>seconds</i> 🔥
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10</b>"""
    
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """
<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v3.0.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    LOGO = """
 ____  ___    ____   __  ____  ____ 
(_  _)/ __)  (  _ \ /  \(_  _)(__  )
  )( ( (_ \   ) _ ((  O ) )(   / _/ 
 (__) \___/  (____/ \__/ (__) (____)
"""
