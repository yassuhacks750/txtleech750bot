#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22849789"))
API_HASH = environ.get("API_HASH", "0fc127c6055acd59f00ec6c229e1e3c4")
BOT_TOKEN = environ.get("BOT_TOKEN", "7627920473:AAFnx6BHFy87yxVbXi4s-n-9ZU3uaFCt5Gs")
OWNER = int(environ.get("OWNER", "7296271316"))
LOG_CHANNEL = "-1002477114210"
CREDIT = "@Professor750bot"
AUTH_USER = os.environ.get('AUTH_USERS', '7296271316').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
