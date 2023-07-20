from django.shortcuts import render
from django.views.generic import ListView

from .models import Product

# Create your views here.
def products_view(request):
    context = {}
    return render(request, 'products/products_list.html', context)

class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 2
    def get_queryset(self):
        return Product.objects.get_active_products()


