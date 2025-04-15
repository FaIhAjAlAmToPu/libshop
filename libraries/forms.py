from django import forms
from .models import Store

class StoreRegistrationForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ('name', 'location', 'address', 'store_type', 'email', 'phone', 'website')
