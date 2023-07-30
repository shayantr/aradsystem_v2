from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse

from ecommerce_cart.forms import UserNewOrderForm
from ecommerce_cart.models import OrderClass, OrderDetailClass
from ecommerce_products.models import Product

# Create your views here.

@login_required
def add_user_order_view(request, product_slug):
    new_order_form = UserNewOrderForm(request.POST or None)
    product_slug = product_slug
    if new_order_form.is_valid():
        order = OrderClass.objects.filter(owner_id=request.user.id, is_payed=False).first()
        if order is None:
            order = OrderClass.objects.create(owner_id=request.user.id, is_payed=False)
        #product = Product.objects.filter(pk=new_order_form.cleaned_data['product_id']).first()
        count = new_order_form.cleaned_data['count']
        products = new_order_form.cleaned_data['product_id']
        product = Product.objects.get(pk=products)
        order.orderid.create(product_id_id=products, price=product.price, count=count)
    return redirect(reverse('product_detail', args=(product_slug,)))
