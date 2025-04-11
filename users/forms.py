from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return cleaned_data


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField()

    def clean_username(self):
        email = self.cleaned_data.get('username')
        try:
            # Find the user by email
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("User with this email does not exist.")
        return user.username  # Use the username for authentication