from django.shortcuts import render, redirect

from pricemonitor.models.serviceproduct import ServiceProduct
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from pricemonitor.permissions import ModeratorPermisionMixin

class ServiceProductList(LoginRequiredMixin, ListView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_list.html"


class ServiceProductCreate(ModeratorPermisionMixin, CreateView):
    model = ServiceProduct
    fields = ['product', 'service', 'product_url']
    template_name = "pricemonitor/serviceproduct_create_form.html"
    success_url = reverse_lazy('serviceproductlist')

    def get_initial(self):
        return {
            'service': self.kwargs['service_id']
        }

    def get_success_url(self):
        return reverse_lazy('servicedetail', args=[self.kwargs['service_id']])


class ServiceProductUpdate(ModeratorPermisionMixin, UpdateView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_update_form.html"
    success_url = reverse_lazy('serviceproductlist')


class ServiceProductDelete(ModeratorPermisionMixin, DeleteView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_delete_form.html"
    success_url = reverse_lazy('serviceproductlist')