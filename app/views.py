from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import pyrebase
from utils import db

def index(request):
    user_name = db.child('card_data').child('Name').get().val()
    context = {
        "user_name": user_name
    }
    return render(request, 'app/base.html', context)

def draft(request):
    return render(request, 'app/draft.html')