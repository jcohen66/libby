from django.contrib import admin
from .models import Author, Book

# Register your models here.
classes = [Author, Book]

for model in classes:
    admin.site.register(model)

