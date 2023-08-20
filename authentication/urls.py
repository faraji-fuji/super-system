from django.urls import path
from authentication import views

urlpatterns=[
    path('user/', views.user_list, name="user_list"),
    path('user/<int:uid>/', views.user_detail, name="user_detail"),
]
