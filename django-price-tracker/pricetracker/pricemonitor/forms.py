from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Service, Product, ServiceProduct
from django.contrib.auth.models import User

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


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(max_length=50, label="Imię", widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=50, label="Nazwisko", widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


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



