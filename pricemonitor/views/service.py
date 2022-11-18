from django.shortcuts import render, redirect

from pricemonitor.models.service import Service
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from pricemonitor.permissions import ModeratorPermisionMixin


class ServiceCreate(ModeratorPermisionMixin, CreateView):
    model = Service
    template_name = "pricemonitor/service_create_form.html"
    fields = ["host", "service_name", "verbose_name"]
    success_url = reverse_lazy('servicelist')


class ServiceList(LoginRequiredMixin, ListView):
    model = Service
    template_name = "pricemonitor/service_list.html"

class ServiceDetail(LoginRequiredMixin, DetailView):
    model = Service
    template_name = 'pricemonitor/service_detail_form.html'
    success_url = reverse_lazy('servicelist')


class ServiceUpdate(ModeratorPermisionMixin, UpdateView):
    model = Service
    template_name = "pricemonitor/service_update_form.html"
    fields = ["host", "service_name", "verbose_name"]
    success_url = reverse_lazy('servicelist')


class ServiceDelete(ModeratorPermisionMixin, DeleteView):
    model = Service
    template_name = "pricemonitor/service_delete_form.html"
    success_url = reverse_lazy('servicelist')

