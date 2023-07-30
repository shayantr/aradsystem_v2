from django.db import models

# Create your models here.
class SiteSettings(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان سایت')
    address = models.CharField(max_length=400, verbose_name='آدرس')
    phone = models.IntegerField(max_length=15, verbose_name='تلفن')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')

    class Meta:
        verbose_name='تنظیمات سایت'
        verbose_name_plural = 'مدیریت سایت'

    def __str__(self):
        return self.title

