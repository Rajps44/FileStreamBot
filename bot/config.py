from os import environ as env
from pymongo import MongoClient

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 27002519))
    API_HASH = env.get("TELEGRAM_API_HASH", "1033ee721101d78366b4ac46aadf3930")
    OWNER_ID = int(env.get("OWNER_ID", 6508598835))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Netflixmovielakh_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "7478730845:AAHt8BoLO0cphbJ6bBkdPxm20Q1PbxBFtq8")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002244711970))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))
    MONGO_URI = env.get("MONGO_URI", "mongodb+srv://t54s2lqiv6:2mOV4n1iL21cMcMH@cluster0.ma3sm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = env.get("DATABASE_NAME", "Cluster0")

    # Shortlink API and URL
    API = env.get("API", "ab210e1aef73dd6b8daf807be471c827792fdeee")
    URL = env.get("URL", "mypowerlinks.org")

    # Verification Settings
    VERIFY_TUTORIAL = env.get("VERIFY_TUTORIAL", "https://t.me/Netflixback_up/122")
    VERIFY = env.get("VERIFY", "True") == "True"

    # MongoDB client setup
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]

    # Collection variables
    users_collection = db['users']

class Server:
    BASE_URL = env.get("BASE_URL", "http://127.0.0.1:8080")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
