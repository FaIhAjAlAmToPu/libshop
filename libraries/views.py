from django.shortcuts import render, get_object_or_404
from .forms import StoreRegistrationForm
from .models import Store

# Create your views here.
def home(request):
    return render(request, 'libraries/index.html')

def register_store(request):
    if request.method == "POST":
        form = StoreRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'libraries/index.html')
    else:
        form = StoreRegistrationForm()
    return render(request, 'libraries/stores_near.html', {'form': form})

def stores(request):
    all_store = Store.objects.all()
    return render(request, 'libraries/stores.html', {'stores': all_store})

def stores_near(request):
    return render(request, 'libraries/stores_near.html')

def store_detail(request):
    store_id = request.GET.get('id')
    store = get_object_or_404(Store, id=store_id)
    return render(request, 'libraries/store_detail.html', {'store': store})