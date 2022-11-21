from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from pricemonitor.models.service import Service
from pricemonitor.models.product import Product
from pricemonitor.models.serviceproduct import ServiceProduct
from pricemonitor.models.userprofile import UserProfile
from django.contrib.auth.models import User

# CRUD - (Cr)eate


class ServiceCreateForm(forms.ModelForm):

    host = forms.CharField(widget=forms.TextInput(attrs={
        'css_class': 'block text-red-700 text-smfont-bold mb-2',
        "class": "input",
        "type": "url",
        "placeholder": "Wprowadż adres URL",
        }), label="Adres URLL")

    service_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Wprowadź nazwę techniczną serwisu",
        }), label="Nazwa techniczna serwisu")

    verbose_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Wprowadź nazwę serwisu",
        }), label="Nazwa serwisu")


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ServiceProductCreateForm(forms.ModelForm):
    class Meta:
        model = ServiceProduct
        fields = '__all__'


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, label="Nazwa użytkownika")
    first_name = forms.CharField(max_length=150, label="Imię")
    last_name = forms.CharField(max_length=150, label="Nazwisko")
    email = forms.EmailField(max_length=150, label="Adres email")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Hasło")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Powtórz hasło")


    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Wprowadź nazwę użytkownika'
        })

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Wprowadź imię'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Wprowadź nazwisko'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Wprowadź swój email'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Podaj hasło'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Potwierdź hasło'
        })


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Wprowadź nazwę użytkownika'
        })
        
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Wprowadź hasło'
        })
    class Meta:
        fields = ['username', 'password']


# CRUD - (U)pdate

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ['avatar']

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



