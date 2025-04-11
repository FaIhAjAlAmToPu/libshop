from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse
from users.forms import SignUpForm, CustomLoginForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = CustomLoginForm