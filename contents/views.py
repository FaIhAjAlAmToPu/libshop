from django.shortcuts import render, get_object_or_404
from .models import Content, Book, Story

def content_list(request):
    contents = Content.objects.all()
    return render(request, 'contents/content_list.html', {'contents': contents})

def content_detail(request, pk):
    content = get_object_or_404(Content, pk=pk)
    return render(request, 'contents/content_detail.html', {'content': content})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'contents/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'contents/book_detail.html', {'book': book})

def story_list(request):
    stories = Story.objects.all()
    return render(request, 'contents/story_list.html', {'stories': stories})

def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    return render(request, 'contents/story_detail.html', {'story': story})
