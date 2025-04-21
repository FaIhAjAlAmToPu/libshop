from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateparse import parse_date

from .models import Content, Book, Story, Author
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
    books = Content.objects.all()
    q = request.GET.get('q')
    if q:
        books = books.filter(title__icontains=q)
    return render(request, 'search/search_book.html', {'books': books})




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




def book_works(request, work):
    # Fetch work details (basic metadata, title, cover, etc.)
    work_response = requests.get(f'https://openlibrary.org/works/{work}.json')
    work_data = work_response.json() if work_response.status_code == 200 else {}

    return render(request, 'contents/book_works.html', {
        'work': work,
        'work_data': work_data
    })

def book_detail_by_edition(request, edition):
    edition_response = requests.get(f'https://openlibrary.org/books/{edition}.json')
    edition_data = edition_response.json() if edition_response.status_code == 200 else {}

    # Check for existing book by isbn_13
    isbn_list = edition_data.get('isbn_13', [])
    if isbn_list:
        book = Book.objects.filter(isbn=isbn_list[0]).first()
        if book:
            return render(request, 'contents/book_detail.html', {'book': book})

    author_name = edition_data.get('authors', [{}])[0].get('name', 'Unknown Author')
    author, _ = Author.objects.get_or_create(name=author_name)

    book = Book.objects.create(
        isbn=edition_data.get('isbn_13', [None])[0] or edition_data.get('isbn_10', [None])[0],
        title=edition_data.get('title', 'Untitled'),
        subtitle=edition_data.get('subtitle', ''),
        year_published=edition_data.get('publish_date'),
        cover_image=f"https://covers.openlibrary.org/b/id/{edition_data['covers'][0]}-L.jpg" if edition_data.get(
        'covers') else '',
        genre=', '.join(edition_data.get('subjects', [])[:3]) if edition_data.get('subjects') else 'Unknown',
        language=edition_data.get('languages', [{}])[0].get('key', 'Unknown').split('/')[-1],
        publishers=', '.join(edition_data.get('publishers', [])),
        author=author
    )

    return render(request, 'contents/book_detail.html', {'book': book})
