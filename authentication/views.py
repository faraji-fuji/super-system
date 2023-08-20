from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication.models import User
from authentication.serializers import CreateUserSerializer


@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all staff, or create a new staff.
    """
    if request.method == 'GET':
        staff = User.objects.all()
        serializer = CreateUserSerializer(staff, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CreateUserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            response_data = serializer.data.copy()
            response_data.pop('password')
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, uid):
    """
    Retrieve, update or delete a user.
    """
    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CreateUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CreateUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

