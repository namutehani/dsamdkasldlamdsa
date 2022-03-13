#(©)Codexbotz

import pyromod.listen
from pyrogram import Client
import sys

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL,FORCE_SUB_CHANNEL1,FORCE_SUB_CHANNEL2,FORCE_SUB_CHANNEL3,FORCE_SUB_CHANNEL4,FORCE_SUB_CHANNEL5,FORCE_SUB_CHANNEL6,FORCE_SUB_CHANNEL7,FORCE_SUB_CHANNEL8 ,CHANNEL_ID
class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                self.LINK = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped.")
                sys.exit()
        if FORCE_SUB_CHANNEL1:
            try:
                link1 = await self.export_chat_invite_link(FORCE_SUB_CHANNEL1)
                self.LINK1 = link1
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL1}")
                self.LOGGER(__name__).info("\nBot Stopped.")
                sys.exit()
        if FORCE_SUB_CHANNEL2:
            try:
                link2 = await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                self.LINK2 = link2
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL2}")
                self.LOGGER(__name__).info("\nBot Stopped.")
                sys.exit() 
        if FORCE_SUB_CHANNEL3:
            try:
                link3 = await self.export_chat_invite_link(FORCE_SUB_CHANNEL3)
                self.LINK3 = link3
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL3}")
                self.LOGGER(__name__).info("\nBot Stopped.")
                sys.exit()
        if FORCE_SUB_CHANNEL4:
            try:
                link4 = await self.export_chat_invite_link(FORCE_SUB_CHANNEL4)
                self.LINK4 = link4
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL4}")
                self.LOGGER(__name__).info("\nBot Stopped.")
                sys.exit() 
        if FORCE_SUB_CHANNEL5:
            try:
                link5 = await self.export_chat_invite_link(FORCE_SUB_CHANNEL5)
                self.LINK5 = link5
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL5}")
                self.LOGGER(__name__).info("\nBot Stopped.")
                sys.exit()
        if FORCE_SUB_CHANNEL6:
            try:
                link6 = await self.export_chat_invite_link(FORCE_SUB_CHANNEL6)
                self.LINK6 = link6
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL1}")
                self.LOGGER(__name__).info("\nBot Stopped.")
                sys.exit()
        if FORCE_SUB_CHANNEL7:
            try:
                link7 = await self.export_chat_invite_link(FORCE_SUB_CHANNEL7)
                self.LINK7 = link7
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL7}")
                self.LOGGER(__name__).info("\nBot Stopped.")
                sys.exit()
        if FORCE_SUB_CHANNEL8:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                self.LINK = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL8}")
                self.LOGGER(__name__).info("\nBot Stopped.")
                sys.exit()                                          
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped.")
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(f"Bot Running..!\n\n")
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
