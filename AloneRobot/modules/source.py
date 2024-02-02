from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from AloneRobot import OWNER_ID, dispatcher
from AloneRobot import pbot as client

Alone = "https://graph.org/file/3c881ce5d6406ce4e7e75.mp4"


@client.on_message(filters.command(["rempo", "sourmce"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Alone,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [sᴛʀᴀɴɢᴇʀ ᴘᴀᴘᴀ](tg://user?id={OWNER_ID})
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**Aʟᴏɴᴇ ✘ Rᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ ",
                        url="\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x41\x4C\x4F\x4E\x45\x5F\x57\x41\x53\x5F\x42\x4F\x54"
                    ),
                    InlineKeyboardButton(
                        "• ᴜᴘᴅᴀᴛᴇ •",
                        url="https://t.me/strangers_bots",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "sᴛʀᴀɴɢᴇʀ"
_help__ = """
 ᴏᴘ ʜᴜ ᴠᴀɪɪɪ 
sᴛʀᴀɴɢᴇʀ ᴏᴘ
"""
