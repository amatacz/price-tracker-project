from django.shortcuts import render, redirect

from pricemonitor.models.serviceproduct import ServiceProduct
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from pricemonitor.permissions import ModeratorPermissionMixin

class ServiceProductList(LoginRequiredMixin, ListView):
    template_name = "pricemonitor/serviceproduct/list.html"

    def get_queryset(self):
        queryset = ServiceProduct.objects.all()
        queryset = queryset.exclude(followed__user = self.request.user.id)
        return queryset


class ServiceProductCreate(ModeratorPermissionMixin, CreateView):
    model = ServiceProduct
    fields = ['product', 'service', 'product_url']
    template_name = "pricemonitor/serviceproduct/create_form.html"
    success_url = reverse_lazy('serviceproductlist')


class ServiceProductUpdate(ModeratorPermissionMixin, UpdateView):
    model = ServiceProduct
    fields = "__all__"
    template_name = "pricemonitor/serviceproduct/update_form.html"
    success_url = reverse_lazy('serviceproductlist')


class ServiceProductDetail(LoginRequiredMixin, DetailView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct/detail.html"


class ServiceProductDelete(ModeratorPermissionMixin, DeleteView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct/delete_form.html"
    success_url = reverse_lazy('serviceproductlist')


class ProductsInServiceProduct(LoginRequiredMixin, ListView):
    model = ServiceProduct

    def get(self, request, pk):
        items = self.model.objects.filter(product__id = pk)
        return render(request, 'pricemonitor/serviceproduct/products_in_serviceproducts_list.html', {'items':items})


class ServiceItemsList(LoginRequiredMixin, ListView):
    model = ServiceProduct

    def get(self, request, pk):
        items = self.model.objects.filter(service__id = pk)
        return render(request, 'pricemonitor/serviceproduct/serviceproducts_in_service_list.html', {'items':items})