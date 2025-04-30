from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from library_shop.borrow.models import BorrowRequest, Borrow
from library_shop.libraries.models import StoreContent


# Create your views here.

def borrow_request(request):
    return render(request, 'borrow_request.html')

def borrow(request):
    return render(request, 'borrow.html')

def borrowed(request):
    return render(request, 'borrowed.html')


@login_required
def send_borrow_request(request, store_content_id):
    store_content = get_object_or_404(StoreContent, pk=store_content_id)
    if request.method == 'POST':
        comment = request.POST.get('comment', '')
        BorrowRequest.objects.create(
            user=request.user,
            storeContent=store_content,
            comment=comment
        )
        return redirect('my_borrowed_books')  # or anywhere you prefer
    return render(request, 'borrow/send_borrow_request.html', {'store_content': store_content})


@login_required
def view_borrow_requests(request):
    requests = BorrowRequest.objects.filter(storeContent__store__profile__user=request.user)
    return render(request, 'borrow/view_borrow_requests.html', {'requests': requests})


@login_required
def approve_borrow_request(request, request_id):
    borrow_req = get_object_or_404(BorrowRequest, pk=request_id)
    Borrow.objects.create(
        user=borrow_req.user,
        storeContent=borrow_req.storeContent,
    )
    borrow_req.delete()
    return redirect('view_borrow_requests')

@login_required
def reject_borrow_request(request, request_id):
    borrow_req = get_object_or_404(BorrowRequest, pk=request_id)
    borrow_req.status = 'rejected'
    borrow_req.save()
    return redirect('view_borrow_requests')


@login_required
def my_borrowed_books(request):
    borrows = Borrow.objects.filter(user=request.user)
    return render(request, 'borrow/my_borrowed_books.html', {'borrows': borrows})


@login_required
def mark_returned(request, borrow_id):
    borrow = get_object_or_404(Borrow, pk=borrow_id)
    borrow.status = 'returned'
    borrow.returned_at = timezone.now()
    borrow.save()
    return redirect('view_borrow_requests')  # or some admin panel
