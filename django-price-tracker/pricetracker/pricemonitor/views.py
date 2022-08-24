from django.shortcuts import render
from .models import Service, Product, ServiceProduct
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# czy widoki Create,Update,Delete z ServiceProduct są potrzebne?


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
    fields = ["host", "name", "verbose_name", "published_data", "updated_datetime"]


class ProductCreate(CreateView):
    model = Product
    template_name = "pricemonitor/product_create_form.html"
    fields = ["name", "verbose_name"]


class ServiceProductCreate(CreateView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_create_form.html"


class ServiceUpdate(UpdateView):
    model = Service
    template_name = "pricemonitor/service_update_form.html"
    fields = ["host", "name", "verbose_name", "published_data", "updated_datetime"]
    success_url = "pricemonitor/service_list.html"


class ProductUpdate(UpdateView):
    model = Product
    template_name = "pricemonitor/product_update_form.html"
    fields = ["name", "verbose_name"]
    success_url = "pricemonitor/product_list.html"


class ServiceProductUpdate(UpdateView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_update_form.html"
    success_url = "pricemonito/serviceproduct_list.html"


class ServiceDelete(DeleteView):
    model = Service
    template_name = "pricemonitor/service_delete_form.html"
    success_url = "pricemonitor/service_list.html"


class ProductDelete(DeleteView):
    model = Product
    template_name = "pricemonitor/product_delete_form.html"
    success_url = "pricemonitor/product_list.html"





