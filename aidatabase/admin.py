from django.contrib import admin
from .models import Book, Series, Ai, Author, Review

admin.site.register(Book)
admin.site.register(Series)
admin.site.register(Ai)
admin.site.register(Author)
admin.site.register(Review)

# aidatabase superuser and passwort