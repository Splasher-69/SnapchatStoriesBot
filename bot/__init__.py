import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "10396473"))
    API_HASH = os.environ.get("API_HASH", "a9a9e84ef6ab7cfa4c5a5e4b758a786a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8000498244:AAGFNl7Mcfw88ZUfeFzbuQ_lVDSz0MN9QXE")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Snapchat_story_saver_69_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
