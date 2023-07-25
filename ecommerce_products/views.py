from django.shortcuts import render
from django.views.generic import ListView
from django.http import *
from django.shortcuts import get_object_or_404

from .models import Product
from ecommerce_tag.models import *
from ecommerce_category.models import *
# Create your views here.
def products_view(request):
    context = {}
    return render(request, 'products/products_list.html', context)

class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 2

    def get_queryset(self):
        category_name = self.kwargs['category']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404("یافت نشد")
        return Product.objects.get_products_bycategory(category_name=category_name)

class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.get_active_products()

def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)

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

def product_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'products/products_categories_partial.html', context)



