

from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "5625170"))
    API_HASH = environ.get("API_HASH", "77633c2757f8697650e0c31cf505ffbc")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Himanshu2k25:Himanshu2k25@@cluster0.2lpqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "vj-forward-bot")
    BOT_OWNER = int(environ.get("BOT_OWNER", "5723551431"))


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

