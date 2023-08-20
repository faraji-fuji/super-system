from django.urls import path, include
from user_roles import views


urlpatterns = [
    path('roles/', views.role_list, name="roles_list"),
    path('roles/<int:pk>/', views.role_detail, name="roles_detail"),

    path('staff/', views.staff_list, name="staff_list"),
    path('staff/<int:pk>/', views.staff_detail, name="staff_detail"),

    path('vendor-staff/', views.vendor_staff_list, name="vendor_staff_list"),
    path('vendor-staff/<int:pk>', views.vendor_staff_detail, name="vendor_staff_detail"),
]