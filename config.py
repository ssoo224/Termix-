import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7365923851:AAEGwQSc7LMONLGCAbRqVNQGtfAoyBewmII")

    APP_ID = int(os.environ.get("APP_ID", 21627756))

    API_HASH = os.environ.get("API_HASH", "fe77fbf0cae9f7f5ece37659e2466cf1")
