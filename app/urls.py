from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # list of acceptable paths
    path('', views.index, name='index'),
    path('draft/', views.draft, name='draft')
]