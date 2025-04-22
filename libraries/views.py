import json

from django.contrib.auth.decorators import login_required
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .forms import StoreRegistrationForm
from .models import Store, StoreContent
from users.models import Profile
from orders.models import Cart
from contents.models import Content, Book

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
            return render(request, 'stores/store_detail.html', {'store': store})
    else:
        form = StoreRegistrationForm()

    return render(request, 'stores/register_store.html', {'form': form})


def stores(request):
    all_store = Store.objects.all()
    return render(request, 'libraries/stores.html', {'stores': all_store})


def set_location(request):
    if request.method == "POST":
        data = json.loads(request.body)
        request.session['latitude'] = data.get('latitude')
        request.session['longitude'] = data.get('longitude')
        print(request.session['latitude'])
        print(request.session['longitude'])
        return JsonResponse({"message": "Location saved successfully!"})
    return JsonResponse({"error": "Invalid request"}, status=400)


def stores_near(request):
    if request.session['latitude'] and request.session['longitude']:
        user_location = Point(request.session['longitude'], request.session['latitude'], srid=4326)
        stores = Store.objects.annotate(distance=D('location', user_location)).order_by('distance')[:10]
    else:
        stores = Store.objects.none()  # No location stored

    return render(request, 'libraries/stores_near.html', {'stores': stores})


@login_required
def store_detail(request):
    store_id = request.GET.get('id')
    store = get_object_or_404(Store, id=store_id)
    query = request.GET.get('q')

    contents = StoreContent.objects.filter(store=store)
    if query:
        contents = contents.filter(content__title__icontains=query)

    return render(request, 'stores/store_detail.html', {
        'store': store,
        'contents': contents,
    })

def search_store(request):
    stores = Store.objects.all()
    q = request.GET.get('q')
    if q:
        stores = stores.filter(name__icontains=q)
    return render(request, 'search/search_store.html', {'stores': stores})


def search_store_content(request):
    q = request.GET.get('q')
    results = StoreContent.objects.select_related('store', 'content')
    if q:
        results = results.filter(content__title__icontains=q)
    return render(request, 'search/search_store_content.html', {'results': results})


def search_near_store_content(request):
    q = request.GET.get('q')
    user_profile = Profile.objects.get(user=request.user)
    user_location = user_profile.last_location
    results = StoreContent.objects.select_related('store', 'content')

    if q:
        results = results.filter(content__title__icontains=q)

    if user_location:
        results = results.annotate(distance=Distance('store__location', user_location)).order_by('distance')

    return render(request, 'search/search_near_store_content.html', {'results': results})


@login_required
def store_content_detail(request, store_content_id):
    store_content = get_object_or_404(StoreContent, id=store_content_id)
    try:
        cart_item = Cart.objects.get(user=request.user, store_content=store_content)
        existing_quantity = cart_item.quantity
    except Cart.DoesNotExist:
        existing_quantity = 1  # default quantity if not already in cart

    return render(request, 'libraries/store_content_detail.html', {
        'store_content': store_content,
        'existing_quantity': existing_quantity,
    })


@login_required
def add_store_content(request, content_id):
    content = get_object_or_404(Content, id=content_id)
    store = request.user.profile.store

    if not store:
        messages.error(request, "You are not assigned to any store.")
        return redirect('home')  # Or your desired redirect

    # Get existing store content if present
    existing = StoreContent.objects.filter(store=store, content=content).first()

    if request.method == 'POST':
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        if existing:
            # Update existing store content
            existing.price = price
            existing.stock = stock
            existing.save()
            messages.success(request, f"{content.title} updated in your store!")
        else:
            # Create new store content
            StoreContent.objects.create(store=store, content=content, price=price, stock=stock)
            messages.success(request, f"{content.title} added to your store!")


        # Redirect conditionally based on content type
        if isinstance(content, Book):
            return redirect('book_detail', pk=content.id)

        return redirect('content_detail', pk=content.id)

    # If not POST, redirect to detail
    if isinstance(content, Book):
        return redirect('book_detail', pk=content.id)

    return redirect('content_detail', pk=content.id)
