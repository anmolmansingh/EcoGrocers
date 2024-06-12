import pyrebase
import os
from dotenv import load_dotenv

#Load environment file for secrets.
try:
    if load_dotenv('.env') is False:
        raise TypeError
except TypeError:
    print('Unable to load .env file.')
    quit()

config = {
    "apiKey": os.environ['API_KEY'],
    "authDomain": os.environ['AUTH_DOMAIN'],
    "databaseURL": os.environ['DATABASE_URL'],
    "projectId": os.environ['PROJECT_ID'],
    "storageBucket": os.environ['STORAGE_BUCKET'],
    "messagingSenderId": os.environ['SENDER_ID'],
    "appId": os.environ['APP_ID']
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()