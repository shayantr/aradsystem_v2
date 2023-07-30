from django.db import models

# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل شما')
    subject = models.CharField(max_length=150, verbose_name='موضوع')
    message = models.TextField(verbose_name='متن')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده')

    class Meta:
        verbose_name = 'فرم های تماس با ما'
        verbose_name_plural = 'فرم تماس با ما'
