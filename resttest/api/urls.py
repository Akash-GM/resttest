
from .views import get_user

from django.urls import path

urlpatterns= [
    path('users/',get_user,name="get_user")
]
