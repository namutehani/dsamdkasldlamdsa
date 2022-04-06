import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, OWNER_ID, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON , HELP_MESSAGE , FORCE_SUB_CHANNEL,FORCE_SUB_CHANNEL1 ,FORCE_SUB_CHANNEL2,FORCE_SUB_CHANNEL3,FORCE_SUB_CHANNEL4,FORCE_SUB_CHANNEL5,FORCE_SUB_CHANNEL6,FORCE_SUB_CHANNEL7,FORCE_SUB_CHANNEL8,FORCE_SUB_CHANNEL9  
from helper_func import subscribed, encode, decode, get_messages
from database.sql import Database
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import random ,string
import time
import datetime
import aiofiles
import traceback
import aiofiles.os
import shutil
import psutil

#=====================================================================================##

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""
uri = "mongodb+srv://odin12:silik10vadisi@cluster0.uvxro.mongodb.net/cluster0?retryWrites=true&w=majority"
db = Database(uri,"TAYFA-BOT")
#=====================================================================================##
def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

async def add_user_to_database(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)

async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        await db.delete_user(user_id)
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        await db.delete_user(user_id)
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"


async def broadcast_handler(m: Message):
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=f"Broadcast Started! You will be notified with log file when all the users are notified."
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(
        total=total_users,
        current=done,
        failed=failed,
        success=success
    )
    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            try:
                sts, msg = await send_msg(
                user_id=int(user['id']),
                message=broadcast_msg
            )
                if msg is not None:
                    await broadcast_log_file.write(msg)
                if sts == 200:
                    success += 1
                else:
                    failed += 1
                if sts == 400:
                    await db.delete_user(user['id'])
                    done += 1
                if broadcast_ids.get(broadcast_id) is None:
                    break
                else:
                    broadcast_ids[broadcast_id].update(
                    dict(
                        current=done,
                        failed=failed,
                        success=success
                    )
                )
            except:
                pass
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"broadcast completed in `{completed_in}`\n\n"
                 f"Total users {total_users}.\n"
                 f"Total done {done}, {success} success and {failed} failed.",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"broadcast completed in `{completed_in}`\n\n"
                    f"Total users {total_users}.\n"
                    f"Total done {done}, {success} success and {failed} failed.",
            quote=True
        )
    await aiofiles.os.remove('broadcast.txt')        
#=====================================================================================##
@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    user_name = '@' + message.from_user.username if message.from_user.username else None
    try:
        await add_user(id, user_name)
    except:
        pass
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Lütfen bekleyin...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Birşeyler yanlış gitti..!")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None
            try:
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup,protect_content=True)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup,protect_content=True)
            except:
                pass
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("😊 Hakkımda", callback_data = "about"),
                    InlineKeyboardButton("🔒 Kapat", callback_data = "close")
                ]
            ]
        )
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    user_name = '@' + message.from_user.username if message.from_user.username else None
    user_id = message.from_user.id
    chat_id = message.chat.id
    channels = [FORCE_SUB_CHANNEL,FORCE_SUB_CHANNEL1 ,FORCE_SUB_CHANNEL2,FORCE_SUB_CHANNEL3,FORCE_SUB_CHANNEL4,FORCE_SUB_CHANNEL5,FORCE_SUB_CHANNEL6,FORCE_SUB_CHANNEL7,FORCE_SUB_CHANNEL8,FORCE_SUB_CHANNEL9]
    sayi = 0
    buttons = [[InlineKeyboardButton(
                "Yardım",
                url="bit.ly/pdfyardim")]]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text = 'Kitabı getir',
                    url = f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass       
    for channel in channels:
       
        if not channel:
            return True
        if user_id in ADMINS:
            return True
        try:
            member = await client.get_chat_member(chat_id=channel,user_id=user_id)
        except UserNotParticipant:
            sayi  += 1
            link = await client.create_chat_invite_link(channel)
            link1=link.invite_link
            se = await client.send_message(chat_id=chat_id,text=f"{sayi}. Kanala katıl ✅.\n🔘 {link1}")
    sw = await message.reply(
        text = FORCE_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        quote = True,
        reply_markup = InlineKeyboardMarkup(buttons),
        disable_web_page_preview = True
    )
@Bot.on_message(filters.command('help') & filters.private & subscribed)
async def help_message(client: Bot,message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=HELP_MESSAGE)
@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text="Hesaplanıyor...") 
    s = await db.total_users_count()
    await msg.edit(f"{s} kişi bu botu kullanıyor.")

@Bot.on_message(filters.command("status") & filters.user(ADMINS) & ~filters.edited)
async def status_handler(_, m: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await m.reply_text(
        text=f"**Toplam disk alanı:** {total} \n"
             f"**Kullanılan Alan:** {used}({disk_usage}%) \n"
             f"**Boş Alan:** {free} \n"
        
             f"**CPU Kullanımı:** {cpu_usage}% \n"
             f"**RAM Kullanımı:** {ram_usage}%\n\n"
             f"**Toplam veritabanındaki kullanıcı sayısı:** `{total_users}`",
        parse_mode="Markdown",
        quote=True
    )    
    
@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def broadcast_in(_, m: Message):
    await broadcast_handler(m)
@Bot.on_message(filters.command('st') & filters.private)
async def start_comnd(client: Client, message: Message):
    chow = -1001769688352
    async for x in client.iter_chat_members(chow):
        id =x.user.id
        user_name = x.user.first_name  
  
        try:
            if not await db.is_user_exist(id):
                await db.add_user(id)
        except:
            print("hata")
