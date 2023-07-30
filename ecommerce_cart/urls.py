from django.urls import path

from ecommerce_cart.views import add_user_order_view

urlpatterns = [
    path('add-user-order/<str:product_slug>', add_user_order_view, name='order_view')
]