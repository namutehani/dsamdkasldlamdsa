#(©)Codexbotz

import base64
import re
import asyncio
from pyrogram import filters
from config import FORCE_SUB_CHANNEL,FORCE_SUB_CHANNEL1,FORCE_SUB_CHANNEL2,FORCE_SUB_CHANNEL3,FORCE_SUB_CHANNEL4,FORCE_SUB_CHANNEL5,FORCE_SUB_CHANNEL6,FORCE_SUB_CHANNEL7,FORCE_SUB_CHANNEL8,FORCE_SUB_CHANNEL9 ,FORCE_SUB_CHANNEL10 , ADMINS
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait

async def is_subscribed(filter, client, update):
    if not FORCE_SUB_CHANNEL:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL, user_id = user_id)
    except UserNotParticipant:
        return False
    
    if not FORCE_SUB_CHANNEL1:
        return True
    try:
        member1 = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL1, user_id = user_id)
    except UserNotParticipant:
        return False
    if not FORCE_SUB_CHANNEL2:
        return True
    try:
        member2 = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL2, user_id = user_id)
    except UserNotParticipant:
        return False
    if not FORCE_SUB_CHANNEL3:
        return True
    try:
        member3 = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL3, user_id = user_id)
    except UserNotParticipant:
        return False
    if not FORCE_SUB_CHANNEL4:
        return True
    try:
        member4 = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL4, user_id = user_id)
    except UserNotParticipant:
        return False
    if not FORCE_SUB_CHANNEL5:
        return True
    try:
        member5 = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL5, user_id = user_id)
    except UserNotParticipant:
        return False
    if not FORCE_SUB_CHANNEL6:
        return True
    try:
        member6 = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL6, user_id = user_id)
    except UserNotParticipant:
        return False
    if not FORCE_SUB_CHANNEL7:
        return True
    try:
        member7 = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL7, user_id = user_id)
    except UserNotParticipant:
        return False
    if not FORCE_SUB_CHANNEL8:
        return True
    try:
        member8 = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL8, user_id = user_id)
    except UserNotParticipant:
        return False
    if not FORCE_SUB_CHANNEL9:
        return True
    try:
        member9 = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL9, user_id = user_id)
    except UserNotParticipant:
        return False
    if not FORCE_SUB_CHANNEL10:
        return True
    try:
        member1 = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL10, user_id = user_id)
    except UserNotParticipant:
        return False
    if not member.status in ["creator", "administrator", "member"]:
        return False
    if not member1.status in ["creator", "administrator", "member"]:
        return False
    if not member2.status in ["creator", "administrator", "member"]:
        return False
    if not member3.status in ["creator", "administrator", "member"]:
        return False
    if not member4.status in ["creator", "administrator", "member"]:
        return False
    if not member5.status in ["creator", "administrator", "member"]:
        return False
    if not member6.status in ["creator", "administrator", "member"]:
        return False
    if not member7.status in ["creator", "administrator", "member"]:
        return False
    if not member8.status in ["creator", "administrator", "member"]:
        return False
    if not member9.status in ["creator", "administrator", "member"]:
        return False
    if not member10.status in ["creator", "administrator", "member"]:
        return False
    else:
        return True
async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    base64_string = (base64_bytes.decode("ascii")).strip("=")
    return base64_string

async def decode(base64_string):
    base64_string = base64_string.strip("=") # links generated before this commit will be having = sign, hence striping them to handle padding errors.
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes) 
    string = string_bytes.decode("ascii")
    return string

async def get_messages(client, message_ids):
    messages = []
    total_messages = 0
    while total_messages != len(message_ids):
        temb_ids = message_ids[total_messages:total_messages+200]
        try:
            msgs = await client.get_messages(
                chat_id=client.db_channel.id,
                message_ids=temb_ids
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
            msgs = await client.get_messages(
                chat_id=client.db_channel.id,
                message_ids=temb_ids
            )
        except:
            pass
        total_messages += len(temb_ids)
        messages.extend(msgs)
    return messages

async def get_message_id(client, message):
    if message.forward_from_chat:
        if message.forward_from_chat.id == client.db_channel.id:
            return message.forward_from_message_id
        else:
            return 0
    elif message.forward_sender_name:
        return 0
    elif message.text:
        pattern = "https://t.me/(?:c/)?(.*)/(\d+)"
        matches = re.match(pattern,message.text)
        if not matches:
            return 0
        channel_id = matches.group(1)
        msg_id = int(matches.group(2))
        if channel_id.isdigit():
            if f"-100{channel_id}" == str(client.db_channel.id):
                return msg_id
        else:
            if channel_id == client.db_channel.username:
                return msg_id
    else:
        return 0

subscribed = filters.create(is_subscribed)
