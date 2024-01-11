from django.contrib import admin
from .models import Category
# Register your models here.

class AdminCategory(admin.ModelAdmin):
    exclude = ("slug",)
    list_display=("category","created_at","updated_at",)
admin.site.register(Category,AdminCategory)
