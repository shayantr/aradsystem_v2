from django.shortcuts import redirect, render

def header_view(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Header.html', {})


def footer_view(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Footer.html', context)


def home_view(request):
    return render(request, 'home_page.html', {})