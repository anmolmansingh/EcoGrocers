import pyrebase

config = {
    "apiKey": "AIzaSyBwB9gA2--WzleGgCfs6lgLHI6sKtI3CwQ",
    "authDomain": "ecogrocers.firebaseapp.com",
    "databaseURL": "https://ecogrocers-default-rtdb.firebaseio.com",
    "projectId": "ecogrocers",
    "storageBucket": "ecogrocers.appspot.com",
    "messagingSenderId": "668707648924",
    "appId": "1:668707648924:web:467bc7e79f762727220459",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()