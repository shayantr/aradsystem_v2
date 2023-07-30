from django import forms
from django.core import validators


class ContactusForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'لطفا نام و نام خانوادگی خود را وارد کنید', 'class': 'form-control'}),
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(150, 'نام و نام خانوادگی نمی تواند بیشتر از ۱۵۰ کاراکتر باشد')
        ]
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'لطفا آدرس ایمیل خود را وارد کنید', 'class': 'form-control'}),
        label='ایمیل',
        validators=[
            validators.MaxLengthValidator(150, 'ایمیل نمی تواند بیشتر از ۱۵۰ کاراکتر باشد')
        ]
    )
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'لطفا موضوع خود را وارد کنید', 'class': 'form-control'}),
        label='موضوع',
        validators=[
            validators.MaxLengthValidator(150, 'موضوع نمی تواند بیشتر از ۱۵۰ کاراکتر باشد')
        ]
    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'لطفا متن پیام خود را وارد کنید', 'class': 'form-control', 'rows': '8'}),
        label='متن پیام',
        validators=[
            validators.MaxLengthValidator(300, 'متن پیام نمی تواند بیشتر از ۳۰۰ کاراکتر باشد')
        ]
    )
