import asyncio
import os
import time
import requests
from config import START_IMG_URL, OWNER_ID
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import app

@app.on_message(filters.text & filters.regex(r"^\.$"))
async def huhh(client: Client, message: Message):
    usr = await client.get_chat(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username

    await message.reply(
        text=f"""<b><a href="https://t.me/{usrnam}">• Dev ↦ {name}</a></b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                        "♪ 𝒔𝒂𝒖𝒅 ♪", url="https://t.me/YMMYC"),
                ],
            ]
        ),
        reply_to_message_id=message.id  # This ensures the bot replies to the user s message
    )
