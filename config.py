from os import environ 

class Config:
    API_ID = environ.get("API_ID", "20373203")
    API_HASH = environ.get("API_HASH", "8962717c7c708e210f66ea658db58d85")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7140730809:AAGKEUOyd-zDgYMkWWaKJ-LfMOq6MtuDEiw") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://sheetuzt23:sheetu@cluster0.qekf8qc.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6994050538').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
