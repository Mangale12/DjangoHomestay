from django.db import models

# Create your models here.
class HomeBanner(models.Model):
    bannerImage = models.ImageField(upload_to="images/", blank=True)
    title = models.CharField(max_length=255, blank=True, unique=True)
    title_description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
class Room(models.Model):
    room_photo = models.ImageField(upload_to="images/", max_length=255, blank=True)
    type = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.type
    
class Service(models.Model):
    icon = models.CharField(max_length=250, blank=True)
    title = models.CharField(max_length=250, blank=True, unique=True)
    description  = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250, blank=True)
    message = models.TextField()
    profile = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Setting(models.Model):
    logo = models.ImageField(upload_to="images/", height_field=None, width_field=None, null=True)
    facebook = models.CharField(max_length=250, null=True)
    insta = models.CharField(max_length=250, null=True)
    address = models.TextField(null=True)
    phone = models.TextField(null=True)
    gemail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    