from django.shortcuts import render, redirect

from pricemonitor.models.service import Service
from pricemonitor.models.serviceproduct import ServiceProduct
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from pricemonitor.permissions import ModeratorPermissionMixin


class ServiceCreate(LoginRequiredMixin, CreateView):
    model = Service
    template_name = "pricemonitor/service/create_form.html"
    fields = ["verbose_name", "host"]
    success_url = reverse_lazy('servicelist')


class ServiceList(LoginRequiredMixin, ListView):
    model = Service
    template_name = "pricemonitor/service/list.html"


class ServiceDetail(LoginRequiredMixin, DetailView):
    model = Service
    template_name = 'pricemonitor/service/detail_form.html'
    success_url = reverse_lazy('servicelist')


class ServiceUpdate(ModeratorPermissionMixin, UpdateView):
    model = Service
    template_name = "pricemonitor/service/update_form.html"
    fields = "__all__"
    success_url = reverse_lazy('servicelist')


class ServiceDelete(ModeratorPermissionMixin, DeleteView):
    model = Service
    template_name = "pricemonitor/service/delete_form.html"
    success_url = reverse_lazy('servicelist')

