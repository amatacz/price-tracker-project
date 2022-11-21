from django.shortcuts import render, redirect

from django.views.generic import View, UpdateView, DeleteView
from django.contrib.auth.views import redirect_to_login
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from pricemonitor.forms import SignUpForm, LoginUserForm

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from pricemonitor.tokens import account_activation_token

from django.contrib.auth.models import User
from pricemonitor.models.userprofile import UserProfile
from django.utils.encoding import force_str
from pricemonitor.tokens import account_activation_token

from django.contrib.auth.mixins import LoginRequiredMixin




# User views
class signUp(View):
    form_class = SignUpForm
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = "Aktywuj swoje konto"
            message = render_to_string('emails/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
                })
            user.email_user(subject, message)

            messages.success(request, "Potwierdź swój email, aby dokończyć rejestrację konta")

            return redirect('login')
        return render(request, self.template_name, {'form': form })


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, ('Twoje konto zostało aktywowane.'))
            return redirect('home')
        else:
            messages.warning(request, ('Link nie działa, prawdopodobnie wygasł lub został już użyty.'))
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


class UserProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'pricemonitor/profile.html'

    def get(self, request):
        user_related_data = User.objects.filter(username = User.username)
        context = {
            "user_related_data": user_related_data
        }
        return render(request, self.template_name, context)

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "pricemonitor/profile_update_form.html"
    fields = ["username", "email"]
    success_url = reverse_lazy('userprofile')

class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'pricemonitor/userprofile_update_form.html'
    fields = ['avatar']
    success_url = reverse_lazy('userprofile')


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "pricemonitor/user_delete_form.html"
    success_url = reverse_lazy('home')