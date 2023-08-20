from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication.models import User
from authentication.serializers import CreateUserSerializer, GetUserSerializer
from authentication.serializers import VerifyOtpSerializer, ResendOtpSerializer
import random
import datetime
from django.utils import timezone
import authentication.utils.helpers as h


def handle_send_sms_message_result(result):
    is_rejected = result.get('is_rejected')
    if is_rejected:
        error = result.get('error')
        return Response({"detail":error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    is_resolved = result.get('is_resolved')
    if is_resolved:
        response = result.get('response')
        return Response(response.json(), response.status_code)
    
    is_successful = result.get('is_successful')
    if is_successful:
        return Response({"detail":"OTP sent successfuly"}, status=status.HTTP_200_OK)



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
            message = f"{user.otp} is your code. Please do not share it with anyone."
            h.send_sms_message(
                phone_number=user.phone_number, 
                message=message)

            return Response({"detail":"OTP regenerated successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"detail":"invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def generate_otp(request):
    if request.method == 'POST':

        serializer = ResendOtpSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')

            user = User.objects.get(email=email)
            user.otp = str(random.randint(100000, 999999))
            user.otp_expiry = timezone.now() + datetime.timedelta(minutes=3)
            user.save()

            # send otp
            message = f"{user.otp} is your code. Please do not share it with anyone."
            result = h.send_sms_message(
                phone_number=user.phone_number, 
                message=message)
            
            return handle_send_sms_message_result(result)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"detail":"invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
                
    