from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from libraries.models import StoreContent
from .models import OrderRequest, Order, Cart
from django.contrib import messages


# Create your views here.

@login_required
def buy(request):
    user = request.user
    order_requests = OrderRequest.objects.get(user=user)
    return render(request, 'orders/buy.html', {'order_requests': order_requests})


@login_required
def add_to_cart(request, store_content_id):
    store_content = get_object_or_404(StoreContent, id=store_content_id)
    quantity = int(request.POST.get('quantity'))

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        storeContent=store_content,
        quantity=quantity
    )

    if not created:
        cart_item.quantity = quantity  # or += quantity for cumulative
        cart_item.save()

    return redirect('cart')

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.storeContent.price * item.quantity for item in cart_items if item.storeContent.price)
    if request.method == 'POST':
        action = request.POST.get('action')
        cart_item_id = request.POST.get('cart_item_id')
        cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
        if action == 'update':
            quantity = int(request.POST.get('quantity', 1))
            cart_item.quantity = quantity
            cart_item.save()

        elif action == 'remove':
            cart_item.delete()
        return redirect('cart')
    return render(request, 'orders/cart.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.storeContent.price * item.quantity for item in cart_items if item.storeContent.price)

    if request.method == 'POST':
        # Check stock availability before processing
        for item in cart_items:
            if item.quantity > item.storeContent.stock:
                messages.error(
                    request,
                    f"Not enough stock for '{item.storeContent.content.title}' in '{item.storeContent.store.name}'. " +
                    f"Available: {item.storeContent.stock}, Requested: {item.quantity}."
                )
                return redirect('cart')

        for item in cart_items:
            OrderRequest.objects.create(
                user=request.user,
                storeContent=item.storeContent,
            )
            item.storeContent.stock -= item.quantity
            item.storeContent.save()
        cart_items.delete()
        return redirect('order_success')  # You can make this a page that says “Thank you!”

    return render(request, 'orders/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def checkout_done(request):
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items:
            messages.error(request, "Your cart is empty.")
            return redirect('checkout')
        for item in cart_items:
            if item.quantity > item.storeContent.stock:
                messages.error(
                    request,
                    f"Not enough stock for '{item.storeContent.content.title}' in '{item.storeContent.store.name}'. "
                    f"Available: {item.storeContent.stock}, Requested: {item.quantity}."
                )
                return redirect('checkout')
            OrderRequest.objects.create(
                user=request.user,
                storeContent=item.storeContent,
                status='ordered'
            )
            item.storeContent.stock -= item.quantity
            item.storeContent.save()
        cart_items.delete()
        messages.success(request, "Order placed successfully!")
        return redirect('checkout')
    return redirect('checkout')


def checkout_error(request):
    return render(request, 'orders/checkout_error.html')

def checkout_cancel(request):
    return render(request, 'orders/checkout_cancel.html')

def checkout_success(request):
    return render(request, 'orders/checkout_success.html')


@login_required
def order_requests(request):
    orderRequests = OrderRequest.objects.filter(user=request.user).order_by('-ordered_at')
    return render(request, 'orders/order_requests.html', {'orderRequests': orderRequests})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def bought(request):
    user = request.user
    orders = Order.objects.get(user=user)
    return render(request, 'orders/bought.html', {'orders': orders})