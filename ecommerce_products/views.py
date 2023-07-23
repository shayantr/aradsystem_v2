from django.shortcuts import render
from django.views.generic import ListView
from django.http import *
from django.shortcuts import get_object_or_404

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

def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    print(product)
    context = {
        'product': product
    }
    return render(request, 'products/product_details.html', context)


class SearchProductsView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 2

    def get_queryset(self):
        request = self.request
        if request.GET:
            query = request.GET.get('q')
            return Product.objects.search(query)



