from django.urls import path

from contactus.views import contactus_view

urlpatterns =[
    path('contactus', contactus_view, name='contactus')
]