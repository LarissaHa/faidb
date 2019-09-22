from django.shortcuts import get_object_or_404, render
from .models import Author, Ai, Review, Book, Series

# Create your views here.

def welcome(request):
    return render(request, 'aidatabase/welcome.html')

def ai_detail(request, key_name):
    # ...
    return render(request, 'ai_detail.html', {'ai': ai}),

def ais(request):
    # ...
    return render(request, 'ais.html', {'ais': ais})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # ...
    return render(request, 'book_detail.html', {'book': book})

def books(request):
    books = Book.objects.all().order_by("publish_year")
    result = []
    for b in books:
        item = {}
        item["book"] = b
        item["authors"] = b.author.all()
        result.append(item)
    return render(request, 'aidatabase/books.html', {'result': result})

def author_detail(request, name):
    author = get_object_or_404(Author, name=name)
    books = Book.objects.filter(author=author.author_id).order_by("publish_year")
    return render(request, 'aidatabase/author_detail.html', {'author': author, 'books': books})

def authors(request):
    authors = Author.objects.all().order_by("name")
    return render(request, 'aidatabase/authors.html', {'authors': authors})

def series_detail(request):
    # ...
    return render(request, 'series_detail.html', {'series': series})

def series(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    # ...
    return render(request, 'series.html', {'series': series})