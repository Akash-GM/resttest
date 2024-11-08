
from .views import get_user,create_user,user_detail

from django.urls import path

urlpatterns= [
    path('users/',get_user,name="get_user"),
    path('users/create_user',create_user,name="create_user"),
    path('users/<int:pk>',user_detail,name="user_detail")

]
