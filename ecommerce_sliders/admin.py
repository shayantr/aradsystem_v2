from django.contrib import admin

from ecommerce_sliders.models import *
# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'img_preview', 'title', 'link']
    list_display_links = ['id', 'title']

admin.site.register(Slider, SliderAdmin)
