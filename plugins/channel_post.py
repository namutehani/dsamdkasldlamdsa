import asyncio
from pyrogram import Client, filters , types
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode

@Bot.on_message(filters.user(ADMINS) & filters.document)
async def channel_post(client: Client, message: Message):
    dosya = message.document
    isim = dosya.file_name
 #   boyut = dosya.file_size
    reply_text = await message.reply_text("Lütfen bekleyin...!", quote = True)
    send_id = -1001769688352
    send_id1 = -1001647428416
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
        converted_id = post_message.message_id * abs(client.db_channel.id)
        string = f"get-{converted_id}"
        base64_string = await encode(string)
        link = f"https://t.me/{client.username}?start={base64_string}"
#       await message.reply(text=f"{isim}")
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
        converted_id = post_message.message_id * abs(client.db_channel.id)
        string = f"get-{converted_id}"
        base64_string = await encode(string)
        link = f"https://t.me/{client.username}?start={base64_string}"
#   await message.reply(text=f"{isim}")
    except Exception as e:
        print(e)
        await reply_text.edit_text("Bir sorun oluştu..!")
        return
    yazi = """
    📁 {isim}
     ────── 〄──────
    │
    ├📥: İndir yazısına tıklayarak
    │gerekli şartları sağlayıp 
    │indirebilirsin. 
    │
    ├  © @tayfaykspdf ❣️ 
    ────── 〄──────
    📤 00:00-06:00 saatleri arasında bot bakımda olduğundan dolayı kapalıdır.
    """.format(isim=isim)
    bosluk = '📥  İndir  📥'
    how_to_download = "❓  Nasıl indirilir ❓"
    paylas = "👥  Kitabı paylaş  👥"
    buttons_markup = [
        [types.InlineKeyboardButton(bosluk, url=f"{link}")],
        [types.InlineKeyboardButton(how_to_download,url=f"https://bit.ly/tayfapdf")],
        [types.InlineKeyboardButton(paylas, url=f'https://telegram.me/share/url?url={link}')]
        ]
    await client.send_message(send_id,f"{yazi}",parse_mode="html", reply_markup = types.InlineKeyboardMarkup(buttons_markup))
    await client.send_message(send_id1,f"{yazi}",parse_mode="html", reply_markup = types.InlineKeyboardMarkup(buttons_markup))
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(bosluk, url=f'{link}')]])
    await reply_text.edit(f"<b>Link burada:</b>\n{link}", reply_markup=reply_markup, disable_web_page_preview = True)
 #   if not DISABLE_CHANNEL_BUTTON:
 #       await message.send_message(text=f"Dosya ismi:\n{isim}",chat_id=client.db_channel.id)
