from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse
from users.forms import SignUpForm, CustomLoginForm
from .models import Profile


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

@login_required
def user_profile(request, pk):
    # user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user_id=pk)
    return render(request, 'users/profile.html', {'profile': profile})