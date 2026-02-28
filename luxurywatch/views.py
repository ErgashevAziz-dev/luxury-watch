from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render
from .models import Product, Banner, Slider


def home(request):
    banners = Banner.objects.all()
    sliders = Slider.objects.all()
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'index.html', {
        'banners': banners,
        'products': products,
        'sliders': sliders,
    })