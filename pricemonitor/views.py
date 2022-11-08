from django.shortcuts import render, redirect

from .models import Service, Product, ServiceProduct, UserProfile
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginUserForm
from rest_framework.exceptions import PermissionDenied


# User views
class signUp(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class loginView(View):
    form_class = LoginUserForm
    template_name = 'registration/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == "POST":
            form = LoginUserForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(
                        request, f"Zalogowałeś się jako {username}")
                    return redirect('home')
                else:
                    messages.error(request, 'Błąd')
            else:
                messages.error(request, "Nazwa użytkownika lub hasło niepoprawne")
        form = LoginUserForm()
        return render(request, 'registration/login.html', {'form':form})

class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(),
                                     self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            message = 'You shall not pass'
            return redirect('home')
            # return message
            #return PermissionDenied('You shall not pass')
             
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)

def home_view(request):
    return render(request, 'pricemonitor/base.html')


class ServiceList(LoginRequiredMixin, ListView):
    model = Service
    template_name = "pricemonitor/service_list.html"


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = "pricemonitor/product_list.html"


class ServiceProductList(LoginRequiredMixin, ListView):
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_list.html"


class ServiceCreate(UserAccessMixin, CreateView):
    permission_required = ('pricemonitor.add_service')
    model = Service
    template_name = "pricemonitor/service_create_form.html"
    fields = ["host", "service_name", "verbose_name"]
    success_url = reverse_lazy('servicelist')


class ServiceDetail(UserAccessMixin, DetailView):
    permission_required = ('pricemonitor.view_service')
    model = Service
    template_name = 'pricemonitor/service_detail_form.html'
    success_url = reverse_lazy('servicelist')


class ServiceUpdate(UserAccessMixin, UpdateView):
    permission_required = ('pricemonitor.change_service')
    model = Service
    template_name = "pricemonitor/service_update_form.html"
    fields = ["host", "service_name", "verbose_name"]
    success_url = reverse_lazy('servicelist')


class ServiceDelete(UserAccessMixin, DeleteView):
    permission_required = ('pricemonitor.delete_service')
    model = Service
    template_name = "pricemonitor/service_delete_form.html"
    success_url = reverse_lazy('servicelist')


class ProductCreate(UserAccessMixin, CreateView):
    permission_required = ('pricemonitor.add_product')
    model = Product
    template_name = "pricemonitor/product_create_form.html"
    fields = ["product_name", "verbose_name"]
    success_url = reverse_lazy('productlist')


class ProductUpdate(UserAccessMixin, UpdateView):
    permission_required = ('pricemonitor.change_product')
    model = Product
    template_name = "pricemonitor/product_update_form.html"
    fields = ["name", "verbose_name"]
    success_url = reverse_lazy('productlist')


class ProductDetail(UserAccessMixin, DetailView):
    permission_required = ('pricemonitor.view_product')
    model = Product
    template_name = 'pricemonitor/product_detail_form.html'
    success_url = reverse_lazy('productlist')


class ProductDelete(UserAccessMixin, DeleteView):
    permission_required = ('pricemonitor.delete_product')
    model = Product
    template_name = "pricemonitor/product_delete_form.html"
    success_url = reverse_lazy('productlist')


class ServiceProductCreate(UserAccessMixin, CreateView):
    permission_required = ('pricemonitor.add_serviceproduct')
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


class ServiceProductUpdate(UserAccessMixin, UpdateView):
    permission_required = ('pricemonitor.change_serviceproduct')
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_update_form.html"
    success_url = reverse_lazy('serviceproductlist')


class ServiceProductDelete(UserAccessMixin, DeleteView):
    permission_required = ('pricemonitor.delete_serviceproduct')
    model = ServiceProduct
    template_name = "pricemonitor/serviceproduct_delete_form.html"
    success_url = reverse_lazy('serviceproductlist')