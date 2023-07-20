from django.urls import path

from ecommerce_products.views import *


urlpatterns = [
    path('products-fbv', products_view),
    path('products', ProductsList.as_view()),
]