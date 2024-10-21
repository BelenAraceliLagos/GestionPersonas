from django.contrib import admin
from .models import Persona

admin.site.register(Persona)
search_fields = ('nombre', 'id')