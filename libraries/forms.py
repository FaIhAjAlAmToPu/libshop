from .models import Store
from django.contrib.gis import forms
from leaflet.forms.widgets import LeafletWidget



class StoreRegistrationForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'location', 'store_type', 'email']

        widgets = {
            'location': LeafletWidget(),
        }

