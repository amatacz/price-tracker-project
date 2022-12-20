from pricemonitor.models.product import Product
from pricemonitor.models.serviceproduct import ServiceProduct
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from pricemonitor.permissions import ModeratorPermissionMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render



class ProductList(ModeratorPermissionMixin, ListView):
    model = Product
    template_name = "pricemonitor/product/list.html"


class ProductCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    template_name = "pricemonitor/product/create_form.html"
    fields = ["verbose_name", "product_URL"]
    success_url = reverse_lazy('serviceproductlist')
    success_message = 'Dziękujemy za dodanie produktu. Produkt będzie widoczny po zatwierdzeniu go przez moderatora.'



class ProductUpdate(ModeratorPermissionMixin, UpdateView):
    model = Product
    template_name = "pricemonitor/product/update_form.html"
    fields = "__all__"
    success_url = reverse_lazy('productlist')


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'pricemonitor/product/detail_form.html'
    success_url = reverse_lazy('productlist')



class ProductDelete(ModeratorPermissionMixin, DeleteView):
    model = Product
    template_name = "pricemonitor/product/delete_form.html"
    success_url = reverse_lazy('productlist')
