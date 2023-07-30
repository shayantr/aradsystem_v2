from django.shortcuts import render
from django.views.generic import ListView
from django.http import *
from django.shortcuts import get_object_or_404
import itertools

from ecommerce_cart.forms import UserNewOrderForm
from .models import *
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

def mygrouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id':product.id,})

    # r_pro = Product.objects.filter(categories__prodcuts=product).distinct()
    #or
    r_pro = Product.objects.get_queryset().filter(categories__prodcuts=product).distinct().exclude(id=product.id)
    grouped_r_pro = mygrouper(3, r_pro)
    galleris = ProductGallery.objects.filter(product_id=product.id)
    g_galleries = list(mygrouper(3, galleris))
    context = {
        'product': product,
        'galleries': g_galleries,
        'related_products': grouped_r_pro,
        'new_order_form': new_order_form,
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




