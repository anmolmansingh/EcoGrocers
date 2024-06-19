from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
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
database = firebase.database()

def homepage(request):
    user_name = database.child('Data').child('Name').get().val()
    footprint = database.child('Data').child('Footprint').get().val()
    type = database.child('Data').child('Type').get().val()
    context = {
        "user_name": user_name,
        "footprint": footprint,
        "type": type
    }
    return render(request, 'app/homepage.html', context)
def get_footprint(request, user_id):
    user_data = database.child('Data').child(user_id).get().val()
    if user_data:
        return render(request, 'app/footprint.html', {'data': user_data})
    else:
        return JsonResponse({'error': 'User not found'}, status=404)