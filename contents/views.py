from django.shortcuts import render, get_object_or_404, redirect
from .models import Content, Book, Story
import requests

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

def search_book(request):
    return render(request, 'contents/search_book.html')




def book_detail_by_isbn(request):
    isbn = request.GET.get('isbn')

    # Check if the book already exists in the database
    books = Book.objects.filter(isbn=isbn)

    if books.exists():
        # If book exists, render the details
        return render(request, 'contents/book_detail.html', {'book': books[0]})

    else:
        # If book does not exist, fetch from Open Library API
        response = requests.get(f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data')

        if response.status_code == 200:
            data = response.json()
            book_data = data.get(f'ISBN:{isbn}')

            if book_data:
                book_details = {
                    'title': book_data.get('title'),
                    'author': ', '.join([author['name'] for author in book_data.get('authors', [])]),
                    'published_date': book_data.get('publish_date'),
                    'cover_image': book_data.get('cover', {}).get('large', 'https://via.placeholder.com/150'),
                    'isbn': isbn
                }


                # Render the book details page with the fetched book data
                return render(request, 'contents/book_openLibrary_detail.html', {'book': book_details})

        # If API request fails or no book found
        return redirect('book_not_found')  # Redirect to a page notifying that the book was not found


def book_not_found(request):
    return render(request, 'contents/book_not_found.html')

def book_create(request):
    return render(request, 'contents/book_create.html')
