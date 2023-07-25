from django.shortcuts import redirect, render

from ecommerce_sliders.models import Slider

def header_view(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/Header.html', context)


def footer_view(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Footer.html', context)


def home_view(request):
    sliders = Slider.objects.all()
    context ={
        'sliders':sliders
    }
    return render(request, 'home_page.html', context)