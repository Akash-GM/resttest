from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

@api_view(['GET'])
def get_user(request):
    users = User.objects.all()
    serialized_users= UserSerializer(users,many= True)
    return Response(serialized_users.data)

@api_view(['POST'])
def create_user(request):

    serialized_data = UserSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data,status=status.HTTP_201_CREATED)
    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)







