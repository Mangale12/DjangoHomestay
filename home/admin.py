from django.contrib import admin
from .models import HomeBanner, Room, Service,Setting,Testimonial
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import admin_thumbnails
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
@admin_thumbnails.thumbnail('bannerImage')
class HomeBanneAdmin(admin.ModelAdmin):
    list_display = ("image_tag","title","status")
    list_editable = ("status",)
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.bannerImage.url))
@admin_thumbnails.thumbnail('room_photo')
class RoomAdmin(admin.ModelAdmin):
    list_display=('image',"type",'created_at')
    def image(self, obj):
        return format_html('<img src="{}" height="100" width="100" />'.format(obj.room_photo.url))
class ServiceAdmin(admin.ModelAdmin):
    list_display=("icon","title","created_at") 
    
    
class SettingAdmin(admin.ModelAdmin):
    list_display=("facebook",)
    def has_add_permission(self, request):
        # Allow adding only if there are no existing records
        if Service.objects.count() == 0:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        # Allow deleting only if there is an existing record
        if Service.objects.count() == 1:
            return True
        return False
    
    def response_add(self, request):
        return HttpResponseRedirect("test")
        # Customize the redirect URL after adding an object
        return self.custom_redirect('add', obj)
    def response_home(self, request):
        return HttpResponseRedirect("hthtt")
        object_id = 1
        change_url = reverse('admin:%s_%s_change' % (self.model._meta.app_label,  self.model._meta.model_name),  args=[object_id])
        return HttpResponseRedirect("hrhrt")
        return redirect(change_url)  
@admin_thumbnails.thumbnail('room_photo')   
class TestimonialAdmin(admin.ModelAdmin):
    list_display=("name","position","profile_pic","created_at",)
    def profile_pic(self, obj):
        return format_html('<img src="{}" height="100" width="100" />'.format(obj.room_photo.url))
admin.site.register(HomeBanner,HomeBanneAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Setting,SettingAdmin)
admin.site.register(Testimonial,TestimonialAdmin)


