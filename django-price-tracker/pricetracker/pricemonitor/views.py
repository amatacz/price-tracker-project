from django.shortcuts import render, redirect

from .models import Service, Product, ServiceProduct, UserProfile
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm


def home_view(request):
    return render(request, 'pricemonitor/base.html')


class ServiceList(LoginRequiredMixin, ListView):
    model = Service
    template_name = "pricemonitor/service_list.html"


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = "pricemonitor/product_list.html"


class ServiceProductList(LoginRequiredMixin, ListView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_list.html"


class ServiceCreate(LoginRequiredMixin, CreateView):
    model = Service
    template_name = "pricemonitor/service_create_form.html"
    fields = ["host", "name", "verbose_name"]
    success_url = reverse_lazy('servicelist')


class ServiceDetail(LoginRequiredMixin, DetailView):
    model = Service
    template_name = 'pricemonitor/service_detail_form.html'
    success_url = reverse_lazy('servicelist')


class ServiceUpdate(LoginRequiredMixin, UpdateView):
    model = Service
    template_name = "pricemonitor/service_update_form.html"
    fields = ["host", "name", "verbose_name"]
    success_url = reverse_lazy('servicelist')


class ServiceDelete(LoginRequiredMixin, DeleteView):
    model = Service
    template_name = "pricemonitor/service_delete_form.html"
    success_url = reverse_lazy('servicelist')


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "pricemonitor/product_create_form.html"
    fields = ["name", "verbose_name", "product_url"]
    success_url = reverse_lazy('productlist')


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "pricemonitor/product_update_form.html"
    fields = ["name", "verbose_name"]
    success_url = reverse_lazy('productlist')


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'pricemonitor/product_detail_form.html'
    success_url = reverse_lazy('productlist')


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "pricemonitor/product_delete_form.html"
    success_url = reverse_lazy('productlist')


class ServiceProductCreate(LoginRequiredMixin, CreateView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_create_form.html"
    success_url = reverse_lazy('serviceproductlist')


class ServiceProductUpdate(LoginRequiredMixin, UpdateView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_update_form.html"
    success_url = reverse_lazy('serviceproductlist')


class ServiceProductDelete(LoginRequiredMixin, DeleteView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_delete_form.html"
    success_url = reverse_lazy('serviceproductlist')


class UserLogin(LoginView):
    model = UserProfile
    template_name = 'registration/login.html'


# class UserCreate(CreateView):
#     form_class = UserCreateForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('home')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Rejestracja przebiegła pomyślnie.")

            return redirect(reverse_lazy('home'))
        messages.error(request, "Rejestracja nie powiodła się. Sprawdź dane.")
    form = NewUserForm()

    return render(request=request, template_name="registration/register.html", context={"register_form": form})

