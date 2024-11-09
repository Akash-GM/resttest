from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

@api_view(['GET'])
def get_user(request):
    users = User.objects.all() # a comment
    #another comment
    serialized_users= UserSerializer(users,many= True)
    return Response(serialized_users.data)


@api_view(['POST'])
def create_user(request):

    serialized_data = UserSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data,status=status.HTTP_201_CREATED)
    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE','GET','PUT'])
def user_detail(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':

        serialized_user = UserSerializer(user)
        return Response(serialized_user.data)

    elif request.method=='PUT':
        serialized = UserSerializer(user, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        print(serialized.errors)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        user.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
        pass

















