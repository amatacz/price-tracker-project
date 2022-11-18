from django.shortcuts import render, redirect

from pricemonitor.models.userprofile import UserProfile
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from pricemonitor.forms import SignUpForm, LoginUserForm

# User views
class signUp(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def post(self, request):
        post = super().post(request)
        username = request.POST["username"]
        password = request.POST["password1"]

        user = authenticate(username=username, password=password)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')


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


def home_view(request):
    return render(request, 'pricemonitor/base.html')

