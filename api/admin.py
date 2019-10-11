from django.contrib import admin
from .models import Letter, Word

# Register your models here.
admin.site.register([Letter, Word])