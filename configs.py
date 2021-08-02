# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = os.environ.get("BOT_OWNER", 1445283714)
    CAPTION = "Rename Bot @{}\n\nMade by @Username_Idarilla"
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))
    START_TEXT = """
__▪️I'm a Telegram File Rename Bot.

▪️Send me a File to Rename.

▪️You Can Also Rename Multiple Files At One Time

⚠️ Don't underestimate about my download speed,

⚠️ My upload speed is above your Guesses

⚠️ Don't Spam Here!__

**Made by @Username_Idarilla**
❗𝐷𝑜𝑛'𝑡 𝐴𝑠𝑘 𝑀𝑦 𝑀𝑎𝑠𝑡𝑒𝑟 𝐹𝑜𝑟 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞❗




    """
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
    """
