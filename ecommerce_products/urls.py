from django.urls import path

from ecommerce_products.views import *


urlpatterns = [
    path('products-fbv/', products_view),
    path('products/', ProductsList.as_view(), name='products'),
    path('products/<str:slug>/', product_detail_view, name='product_detail'),
    path('products/search', SearchProductsView.as_view()),
    path('products/<str:category>', ProductsListByCategory.as_view(), name='product_category'),
    path('product_categories_partial', product_categories_partial, name='product_categories_partial')
]

