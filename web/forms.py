from django import forms
from web.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'price', 'description', 'category','image']