from django.shortcuts import render

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
    # ...
    return render(request, 'books.html', {'books': books})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    # ...
    return render(request, 'author_detail.html', {'author': author})

def authors(request):
    # ...
    return render(request, 'authors.html', {'authors': authors})

def series_detail(request):
    # ...
    return render(request, 'series_detail.html', {'series': series})

def series(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    # ...
    return render(request, 'series.html', {'series': series})