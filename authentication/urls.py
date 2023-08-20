from django.urls import path
from authentication import views

urlpatterns=[
    path('user/', views.user_list, name="user_list"),
    path('user/<int:uid>/', views.user_detail, name="user_detail"),
    path('verify-otp/', views.verify_otp, name="verify_otp"),
    path('resend-otp/', views.resend_otp, name="resend_otp"),
]
