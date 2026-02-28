from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render
from .models import Product, Banner, Slider
from django.core.paginator import Paginator


def home(request):
    banners = Banner.objects.all()
    sliders = Slider.objects.all()
    paginator = Paginator(sliders, 4)  # har sahifada 4 ta item
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    products = Product.objects.all().order_by('-created_at')

    return render(request, 'index.html', {
        'banners': banners,
        'products': products,
        'sliders': sliders,
        'page_obj': page_obj,
    })