from django import forms
from .models import Service, Product, ServiceProduct

# CRUD - (Cr)eate


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ServiceProductCreateForm(forms.ModelForm):
    class Meta:
        model = ServiceProduct
        fields = '__all__'


# CRUD - (U)pdate

class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ServiceProductUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceProduct
        fields = '__all__'
