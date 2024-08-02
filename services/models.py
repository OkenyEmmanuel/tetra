from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import os

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.user.username:
        filename = 'user_Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename) 
   
class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    profile_Pic = models.ImageField(upload_to=path_and_rename,verbose_name="Profile Picture", blank=True)
    
    service_subscriber = 'service_subscriber'
    service_user = 'service_user'
    servicer_provider = 'servicer_provider'
    
    user_types = [
        ( service_subscriber, 'service_subscriber'),
        ( service_user,  'service_user'),
        (servicer_provider, 'servicer_provider')
    ]
    user_type = models.CharField(max_length=30, choices=user_types, default=service_user)
    
    def __str__(self):
        return self.user.username