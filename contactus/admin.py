from django.contrib import admin

# Register your models here.
from contactus.models import Contactus

class ContactusAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read']
    search_fields = ['name', 'message']

admin.site.register(Contactus, ContactusAdmin)
