from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_roles.models import Role, VendorStaff, Staff
from user_roles.serializers import RoleSerializer, StaffSerializer, VendorStaffSerializer


@api_view(['GET', 'POST'])
def role_list(request):
    """
    List all roles, or create a new role.
    """
    if request.method == 'GET':
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def role_detail(request, pk):
    """
    Retrieve, update or delete a role.
    """
    try:
        role = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoleSerializer(role)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RoleSerializer(role, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET', 'POST'])
def staff_list(request):
    """
    List all staff, or create a new staff.
    """
    if request.method == 'GET':
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def staff_detail(request, pk):
    """
    Retrieve, update or delete a staff.
    """
    try:
        staff = Staff.objects.get(pk=pk)
    except Staff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StaffSerializer(staff)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StaffSerializer(staff, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def vendor_staff_list(request):
    """
    List all vendor_staff, or create a new vendor_staff.
    """
    if request.method == 'GET':
        vendor_staff = VendorStaff.objects.all()
        serializer = VendorStaffSerializer(vendor_staff, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VendorStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def vendor_staff_detail(request, pk):
    """
    Retrieve, update or delete a vendor_staff.
    """
    try:
        vendor_staff = VendorStaff.objects.get(pk=pk)
    except VendorStaff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VendorStaffSerializer(vendor_staff)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VendorStaffSerializer(vendor_staff, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vendor_staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    