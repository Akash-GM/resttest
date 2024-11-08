
from .views import get_user,create_user

from django.urls import path

urlpatterns= [
    path('users/',get_user,name="get_user"),
    path('users/create_user',create_user,name="create_user")
]
