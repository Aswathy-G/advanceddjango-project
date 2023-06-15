from django import forms
from web.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','price', 'description', 'image']

        widgets = {
          
            "title" : forms.TextInput(attrs={'class':"input"}),
            "description" : forms.Textarea(attrs={'class':"input"}),
        }
        error_messages = {
            "title" : {
                "required" : "Title field is required"
            },
            "description" : {
                "required" : "Description field is required",
            },
            "image" : {
                "required" : "featured image field is required",
            },
           

        }