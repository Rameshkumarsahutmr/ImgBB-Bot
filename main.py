import asyncio
import os
import shutil
import time
import traceback

import imgbbpy
import pyromod.listen
from pyrogram import Client, filters
from pyrogram.types import ChatAction  # Update this import
from pyromod.helpers import ikb

from utils.configs import Tr, Var

Imgclient = imgbbpy.SyncClient(Var.API)

ext = tuple(
    [".jpg", ".png", ".jpeg", ".wepb", ".gif", ".bmp", ".heic", ".pdf", ".tif", ".webp"]
)

Img = Client(
    "ImgBB Bot",
    bot_token=Var.BOT_TOKEN,
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
)

# ... (rest of your code remains unchanged)

@Img.on_message(
    filters.private
    & (filters.photo | filters.sticker | filters.document | filters.animation)
)
async def getimglink(c, m):
    chat_id = m.from_user.id
    user = await c.get_users(int(chat_id))

    if not Var.API:
        return await m.reply_text(
            Tr.ERR_TEXT,
            quote=True,
        )

    if m.document:
        if not m.document.file_name.endswith(ext):
            return
    await m.reply_chat_action(ChatAction.TYPING)  # Fixed this line
    BTN = ikb(
        # ... (rest of your code remains unchanged)
    )

    await m.reply_text(
        "🗑 AutoDelete ? ...",
        reply_markup=BTN,
        quote=True,
    )

# ... (rest of your code remains unchanged)

Img.run()
