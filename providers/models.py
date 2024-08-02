from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import os
from django.utils import timezone
def path_and_name(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.provider_id:
        filename = 'user_Profile_Pictures/{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename) 

def jumps_and_name(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.doctor_id:
        filename = 'jump_Profile_Pictures/{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename) 

def jump_and_name(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.name:
        filename = 'jump_Profile_Pictures/{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename) 

def save_video_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.provider_id:
        filename = 'User_videos/{}.{}'.format(instance.provider_id, ext)
    return os.path.join(upload_to, filename) 

def save_image_file(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.provider_id:
        filename = 'User_pictures/{}.{}'.format(instance.provider_id, ext)
    return os.path.join(upload_to, filename) 

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    depimg = models.ImageField(upload_to=jump_and_name, verbose_name="Jump Profile", blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Department_Details(models.Model):
    category_id = models.CharField(max_length=100, unique=True)  
    name =  models.CharField(max_length=100, null=True) 
    slug = models.SlugField(null=True, blank=True)
    service = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='cat')
    about = models.TextField(max_length=900, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_id)
        super().save(*args, **kwargs)

class Doctor(models.Model):
    doctor_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    category = models.ForeignKey(Department_Details, on_delete=models.CASCADE, related_name='describe')
    service = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="dc") 
    doctor_pic = models.ImageField(upload_to=jumps_and_name, verbose_name="Provider Profile", blank=True)
    about = models.TextField(max_length=500, blank=True)
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.doctor_id)
        super().save(*args, **kwargs)

class ClientAppointment(models.Model):
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    telephone = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=10, null=True)
    date_of_appointment = models.DateField(null=True)
    time_of_appointment = models.TimeField(null=True)
    reason = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.firstname} - {self.date_of_appointment} at {self.time_of_appointment}"

    def save(self, *args, **kwargs):
        if not self.pk:
            # If it's a new instance, set the creation timestamp
            self.created_at = timezone.now()
        self.updated_at = timezone.now()  # Update timestamp every time the object is saved
        super().save(*args, **kwargs)