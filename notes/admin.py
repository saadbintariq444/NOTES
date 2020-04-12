from django.contrib import admin

# Register your models here.
# here we register the models of database

from .models import Note

admin.site.register(Note)