from django.shortcuts import render

from .models import Service, Product, ServiceProduct
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


def home_view(request):
    return render(request, 'pricemonitor/base.html')


class ServiceList(ListView):
    model = Service
    template_name = "pricemonitor/service_list.html"


class ProductList(ListView):
    model = Product
    template_name = "pricemonitor/product_list.html"


class ServiceProductList(ListView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_list.html"


class ServiceCreate(CreateView):
    model = Service
    template_name = "pricemonitor/service_create_form.html"
    fields = ["host", "name", "verbose_name"]
    success_url = reverse_lazy('servicelist')


class ProductCreate(CreateView):
    model = Product
    template_name = "pricemonitor/product_create_form.html"
    fields = ["name", "verbose_name"]
    success_url = reverse_lazy('productlist')


class ServiceProductCreate(CreateView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_create_form.html"
    success_url = reverse_lazy('serviceproduct_list')


class ServiceUpdate(UpdateView):
    model = Service
    template_name = "pricemonitor/service_update_form.html"
    fields = ["host", "name", "verbose_name"]
    success_url = reverse_lazy('service_list')


class ProductUpdate(UpdateView):
    model = Product
    template_name = "pricemonitor/product_update_form.html"
    fields = ["name", "verbose_name"]
    success_url = reverse_lazy('productlist')


class ServiceProductUpdate(UpdateView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_update_form.html"
    success_url = reverse_lazy('serviceproduct_list')


class ServiceDelete(DeleteView):
    model = Service
    template_name = "pricemonitor/service_delete_form.html"
    success_url = reverse_lazy('service_list')


class ProductDelete(DeleteView):
    model = Product
    template_name = "pricemonitor/product_delete_form.html"
    success_url = reverse_lazy('productlist')


class ServiceProductDelete(DeleteView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_delete_form.html"
    success_url = reverse_lazy('serviceproduct_list')





