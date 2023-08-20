from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication.models import User
from authentication.serializers import CreateUserSerializer, GetUserSerializer
from authentication.serializers import VerifyOtpSerializer, ResendOtpSerializer
import random
import datetime
from django.utils import timezone

@api_view(['GET', 'POST'])
def user_list(request):
    """9
    List all staff, or create a new staff.
    """
    if request.method == 'GET':
        staff = User.objects.all()
        serializer = GetUserSerializer(staff, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CreateUserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            response_data = serializer.data.copy()
            response_data.pop('password')

            # send otp
            
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
        serializer = GetUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GetUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def verify_otp(request):
    if request.method == 'POST':
        serializer = VerifyOtpSerializer(data=request.data)

        if serializer.is_valid():
            request_otp = serializer.validated_data.get('otp')
            email = serializer.validated_data.get('email')
         
            user = User.objects.get(email=email)

        
            if user.otp == request_otp and not user.has_otp_expired():
                user.mark_phone_as_verified()
                return Response({'detail': 'OTP verified and phone number marked as verified.'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid OTP or expired OTP.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"detail":"invalid request methos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def resend_otp(request):
    if request.method == 'POST':

        serializer = ResendOtpSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')

            user = User.objects.get(email=email)

            user.otp = str(random.randint(100000, 999999))
            user.otp_expiry = timezone.now() + datetime.timedelta(minutes=3)
            user.save()

            # send otp

            
            return Response({"detail":"OTP regenerated successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"detail":"invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        



        
    