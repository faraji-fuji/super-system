from rest_framework import serializers
from user_roles.models import Role, Staff, VendorStaff


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class VendorStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorStaff
        fields = '__all__'

