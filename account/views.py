from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from .forms import SignUpForm
from django.contrib.auth import authenticate, login


class LoginViews(LoginView):
    template_name = 'login.html'


class LogoutViews(LogoutView):
    template_name = 'logout.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', context=dict(form=form))
