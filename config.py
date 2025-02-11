""" !/usr/bin/env python3
    -*- coding: utf-8 -*-
    Name     : inline-tube-mate [ Telegram ]
    Repo     : https://github.com/m4mallu/inine-tube-mate
    Author   : Renjith Mangal [ https://t.me/space4renjith ]
    Credits  : https://github.com/SpEcHiDe/AnyDLBot """

import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5107368431:AAFoayQX2CWtLh76Zc76lVopLXwUkeRl6Qs")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "19088110"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "321313266df430b18a704161c96bcf42")

    # Authorized user ids to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # superusers to broadcast messages & fetch subscribers count
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "1287276743").split())

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgresql://postgres:nZeWBRDQcuOxNe5QyIwG@containers-us-west-21.railway.app:7319/railway")

    # Force subscribe channel / group id starting with -100
    FORCE_SUB_CHAT = os.environ.get("FORCE_SUB_CHAT", "-1001235572961")

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
