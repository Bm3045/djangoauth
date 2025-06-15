from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

USER_TYPES = (
    ('doctor', 'Doctor'),
    ('patient', 'Patient'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/')
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
