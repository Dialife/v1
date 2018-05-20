from django.contrib import admin

from .models import Recipe
from .models import Exercise


admin.site.register(Recipe)
admin.site.register(Exercise)