from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeBanner, Testimonial,Service,Setting,Room

def index(request):
    homebanners = HomeBanner.objects.filter(status=True)
    rooms = Room.objects.filter()
    services = Service.objects.filter()
    context = {
        'homebanners':homebanners,
        'rooms':rooms,
        'services':services,
        
    }
    return render(request, 'frontend/index.html', context)
