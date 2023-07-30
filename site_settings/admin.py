from django.contrib import admin

# Register your models here.
from site_settings.models import SiteSettings

admin.site.register(SiteSettings)
