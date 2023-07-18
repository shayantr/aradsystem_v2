from django import forms
from django.contrib.auth import get_user_model
from django.core import validators

User = get_user_model()
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'نام کاربری'}),
        label='نام کاربری'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز خود را وارد نمایید.'}),
        label='رمز عبور'
    )

    # def clean_username(self):
    #     data = self.cleaned_data
    #     if not User.objects.filter(username=data['username']):
    #         self.add_error('username', 'نام کاربری {user} وجود ندارد'.format(user=data['username']))
    #     else:
    #         return data['username']

    def clean_password(self):
        data = self.cleaned_data
        if User.objects.filter(username=data['username']):
            if not User.objects.filter(password=data['password']):
                self.add_error('password', 'رمز عبور اشتباه است.')
            else:
                return data['password']


class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'نام کاربری'}),
        label='نام کاربری',
        validators=[
            validators.MinLengthValidator(3,'تعداد کارکتر های وارد شده نباید کمتر از ۳ تا باشد'),
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'ایمیل خود را وارد نمایید'}),
        label='ایمیل'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز خود را وارد نمایید.'}),
        label='رمز عبور'
    )
    password_2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خود را تایید کنید.'}),
        label='تکرار رمز عبور'
    )

    def clean_password_2(self):
        password = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_2']
        if password != password_2:
            self.add_error('password_2', 'رمز وارد شده یکی نیست')
        return password_2

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data):
            raise forms.ValidationError("این اسم قبلا وجود دارد")
        return data


