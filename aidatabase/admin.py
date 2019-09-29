from django.contrib import admin
from .models import Ai, Person, Review, Source  # , Series

# admin.site.register(Book)
# admin.site.register(Series)
admin.site.register(Ai)
admin.site.register(Person)
admin.site.register(Review)
admin.site.register(Source)

# aidatabase superuser and passwort