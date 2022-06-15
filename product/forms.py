from django import forms
from product.models import ProductA

class ProductAdd(forms.ModelForm):
    original_name = forms.CharField(required=True)
    
    class Meta:
        model = ProductA
        fields = ('original_name',)
