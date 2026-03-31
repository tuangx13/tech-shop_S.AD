from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StaffRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class LaptopForm(forms.Form):
    name = forms.CharField(max_length=255)
    brand = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=12, decimal_places=2)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    cpu = forms.CharField(max_length=100, required=False)
    ram = forms.CharField(max_length=50, required=False)
    storage = forms.CharField(max_length=100, required=False)
    screen_size = forms.CharField(max_length=50, required=False)
    stock = forms.IntegerField(min_value=0)
    image_url = forms.URLField(required=False)


class MobileForm(forms.Form):
    name = forms.CharField(max_length=255)
    brand = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=12, decimal_places=2)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    cpu = forms.CharField(max_length=100, required=False)
    ram = forms.CharField(max_length=50, required=False)
    storage = forms.CharField(max_length=100, required=False)
    screen_size = forms.CharField(max_length=50, required=False)
    battery = forms.CharField(max_length=50, required=False)
    stock = forms.IntegerField(min_value=0)
    image_url = forms.URLField(required=False)
