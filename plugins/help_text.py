#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from pyrogram import (
    Client,
    Filters,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

@pyrogram.Client.on_callback_query()
async def cb_handler(bot, update):

    if "start" in update.data: 
        await update.message.delete() 
        await start(bot, update.message)

    if "close" in update.data:
        await update.message.delete()

    if "help_back" in update.data: 
        await update.message.delete() 
        await help_user(bot, update.message)

    if "about" in update.data: 
        await update.message.delete() 
        await about_me(bot, update.message)


@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🔰 creater', url="t.me/DeathCaptureBoy")
                    
                ],
                [
                    InlineKeyboardButton('❔Help', callback_data="help_back"),
                    InlineKeyboardButton('❗About', callback_data="about"),
                    InlineKeyboardButton('🔐Close', callback_data="close")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def about_me(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/about")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_ME,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🔙Back', callback_data="help_back"),
                    InlineKeyboardButton('🔐Close', callback_data="close")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [  
                    InlineKeyboardButton('🛡️Share', url="tg://msg?text=Hai%20Friend%20%E2%9D%A4%EF%B8%8F%2C%0AToday%20i%20just%20found%20out%20an%20intresting%20and%20Powerful%20%2A%2ARename%20Bot%2A%2A%20for%20Free%F0%9F%A5%B0.%20%0A%2A%2ABot%20Link%20%3A%2A%2A%20%40KL35RenamerBot%20%F0%9F%94%A5")
                ],
                [
                    InlineKeyboardButton('🔰 Creater', url="t.me/DeathCaptureBoy")   
                ],
                [
                    InlineKeyboardButton('❔Help', callback_data="help_back"),
                    InlineKeyboardButton('🔐Close🔐', callback_data="close")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/upgrade")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🔐Close', callback_data="close")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["bots"]))
async def kl35thumb(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.photo, "/bots")
    await bot.send_photo(
        chat_id=update.chat.id,
        photo=Translation.KL35_THUMBNAIL_PHOTO,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('❔Help', callback_data="help_back"),
                    InlineKeyboardButton('🔐Close', callback_data="close")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )
