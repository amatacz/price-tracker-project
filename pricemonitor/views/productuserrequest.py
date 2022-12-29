from django.contrib.auth.mixins import LoginRequiredMixin
from pricemonitor.permissions import ModeratorPermissionMixin
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# from pricemonitor.forms import ProductUserRequestForm




# class ProductUserRequestCreate(LoginRequiredMixin, CreateView):
#     form_class = ProductUserRequestForm
#     template_name = 'pricemonitor/productuserrequest/create_form.html'
#     success_url = reverse_lazy('productlist')


#     def get(self, request):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form}) 


# class ProductUserRequestList(ModeratorPermissionMixin, ListView):
#     model = ProductUserRequest
#     template_name = 'pricemonitor/productuserrequest/list.html'


# class ProductUserRequestDetail(ModeratorPermissionMixin, DetailView):
#     model = ProductUserRequest
#     template_name = 'pricemonitor/productuserrequest/detail_form.html'
#     success_url = reverse_lazy('productuserrequestlist')

# class ProductUserRequestDelete(ModeratorPermissionMixin, DeleteView):
#     model = ProductUserRequest
#     template_name = 'pricemonitor/productuserrequest/delete_form.html'
#     success_url = reverse_lazy('productuserrequestlist')
