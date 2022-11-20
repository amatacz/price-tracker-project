from django.shortcuts import render, redirect

from pricemonitor.models.product import Product
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from pricemonitor.permissions import ModeratorPermisionMixin

class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = "pricemonitor/product_list.html"


class ProductCreate(ModeratorPermisionMixin, CreateView):
    model = Product
    template_name = "pricemonitor/product_create_form.html"
    fields = ["product_name", "verbose_name"]
    success_url = reverse_lazy('productlist')


class ProductUpdate(ModeratorPermisionMixin, UpdateView):
    model = Product
    template_name = "pricemonitor/product_update_form.html"
    fields = ["product_name", "verbose_name"]
    success_url = reverse_lazy('productlist')


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'pricemonitor/product_detail_form.html'
    success_url = reverse_lazy('productlist')


class ProductDelete(ModeratorPermisionMixin, DeleteView):
    model = Product
    template_name = "pricemonitor/product_delete_form.html"
    success_url = reverse_lazy('productlist')
