from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.category