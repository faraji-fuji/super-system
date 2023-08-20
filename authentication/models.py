from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
import datetime
import random


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    otp = models.IntegerField(null=True)
    otp_expiry = models.DateTimeField(null=True)
    last_login = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def has_otp_expired(self):
        return self.otp_expiry <= timezone.now()

    def mark_as_verified(self):
        self.is_verified = True
        self.save()

    def mark_email_as_verified(self):
        self.is_email_verified = True
        self.save()

    def mark_phone_as_verified(self):
        self.is_phone_verified = True
        self.save()

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        print(f"PASSWORD: {self.password}")

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.otp = str(random.randint(100000, 999999)) 
            self.otp_expiry = timezone.now() + datetime.timedelta(minutes=3)
        super(User, self).save(*args, **kwargs)


