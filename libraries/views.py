from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import StoreRegistrationForm
from .models import Store
from users.models import Profile

# Create your views here.
def home(request):
    return render(request, 'libraries/index.html')



@login_required
def register_store(request):
    if request.method == 'POST':
        form = StoreRegistrationForm(request.POST)
        if form.is_valid():
            store = form.save()
            # Assign the store to the user's profile
            profile = Profile.objects.get(user=request.user)
            profile.store = store
            profile.save()
            return redirect('store_detail', store)  # make sure this URL/view exists
    else:
        form = StoreRegistrationForm()

    return render(request, 'stores/register_store.html', {'form': form})


def stores(request):
    all_store = Store.objects.all()
    return render(request, 'libraries/stores.html', {'stores': all_store})

def stores_near(request):
    return render(request, 'libraries/stores_near.html')

def store_detail(request):
    store_id = request.GET.get('id')
    store = get_object_or_404(Store, id=store_id)
    return render(request, 'libraries/store_detail.html', {'store': store})