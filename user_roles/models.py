from django.db import models

class Role(models.Model):
    permission = models.CharField(max_length=1024)
    name = models.CharField(max_length=256)

class Staff(models.Model):
    user_id = models.CharField(max_length=255)
    role_id = models.CharField(max_length=255)

class VendorStaff(models.Model):
    vendor_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    role_id = models.CharField(max_length=255)

