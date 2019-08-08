from django.contrib import admin
from .models import Book, Series, Ai, Author

admin.site.register(Book)
admin.site.register(Series)
admin.site.register(Ai)
admin.site.register(Author)

# aidatabase superuser and passwort