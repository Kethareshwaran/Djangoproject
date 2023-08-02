from django import forms
from .models import Product
from django.forms import ModelForm,models
class Form(ModelForm):
    class Meta:
        model = User
        fields = "_all_"

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class OrderForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['order_status', 'items']

