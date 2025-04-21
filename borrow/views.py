from django.shortcuts import render

# Create your views here.

def borrow_request(request):
    return render(request, 'borrow_request.html')

def borrow(request):
    return render(request, 'borrow.html')

def borrowed(request):
    return render(request, 'borrowed.html')
