from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from .forms import LoginForm
from .forms import RegisterForm

# Redirect root / based on authentication
class HomeRedirectView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return redirect('login')


# Login using a custom form and CBV
class LoginFormView(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('dashboard')
        return render(request, self.template_name, {'form': form})


# Logout view using built-in LogoutView CBV
class LogoutFormView(DjangoLogoutView):
    next_page = 'login'  # redirect after logout

class RegisterFormView(View):
    template_name = 'accounts/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect('dashboard')
        return render(request, self.template_name, {'form': form})

