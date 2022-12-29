from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


from django.contrib.auth.models import User
from pricemonitor.models.userserviceproduct import UserServiceProduct
from pricemonitor.models.serviceproduct import ServiceProduct


class UserServiceProductCreate(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        service_product = ServiceProduct.objects.get(pk=pk)
        user_serviceproduct = UserServiceProduct.objects.filter(user=request.user, service_product=service_product)
        if user_serviceproduct.exists():
            messages.error(request, 'Już obserwujesz ten produkt')
        else:
            UserServiceProduct(user=request.user, service_product=service_product).save()
            messages.success(request, "Dodano!")
        return redirect('serviceproductlist')


class UserServiceProductList(LoginRequiredMixin, ListView):
    model = UserServiceProduct
    template_name = "pricemonitor/userserviceproduct/list.html"


class UserServiceProductDelete(LoginRequiredMixin, DeleteView):
    def get(self, request, pk, *args, **kwargs):
        user_serviceproduct = UserServiceProduct.objects.get(pk=pk)
        user_serviceproduct.delete()
        messages.success(request, "Przestałeś obserwować ten produkt")
        return redirect('userserviceproductlist')
