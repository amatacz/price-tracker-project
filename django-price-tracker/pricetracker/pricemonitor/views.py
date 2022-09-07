from django.shortcuts import render

from .models import Service, Product, ServiceProduct
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse


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


class ServiceDetail(DetailView):
    model = Service
    template_name = 'pricemonitor/service_detail_form.html'
    success_url = reverse_lazy('servicelist')


class ServiceUpdate(UpdateView):
    model = Service
    template_name = "pricemonitor/service_update_form.html"
    fields = ["host", "name", "verbose_name"]
    success_url = reverse_lazy('servicelist')


class ServiceDelete(DeleteView):
    model = Service
    template_name = "pricemonitor/service_delete_form.html"
    success_url = reverse_lazy('servicelist')

    # def delete(self, request, *args):
    #     service = Service.objects.get(pk=id)
    #     service.delete()
    #     return HttpResponse("Deleted!")


class ProductCreate(CreateView):
    model = Product
    template_name = "pricemonitor/product_create_form.html"
    fields = ["name", "verbose_name", "product_url"]
    success_url = reverse_lazy('productlist')


class ProductUpdate(UpdateView):
    model = Product
    template_name = "pricemonitor/product_update_form.html"
    fields = ["name", "verbose_name"]
    success_url = reverse_lazy('productlist')


class ProductDetail(DetailView):
    model = Product
    template_name = 'pricemonitor/product_detail_form.html'
    success_url = reverse_lazy('productlist')


class ProductDelete(DeleteView):
    model = Product
    template_name = "pricemonitor/product_delete_form.html"
    success_url = reverse_lazy('productlist')


class ServiceProductCreate(CreateView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_create_form.html"
    success_url = reverse_lazy('serviceproductlist')


class ServiceProductUpdate(UpdateView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_update_form.html"
    success_url = reverse_lazy('serviceproductlist')


class ServiceProductDelete(DeleteView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_delete_form.html"
    success_url = reverse_lazy('serviceproductlist')








