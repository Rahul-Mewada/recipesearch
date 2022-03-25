from django.contrib import admin
from .models import Recipe, VisitedUrl
# Register your models here.

admin.site.register(Recipe)
admin.site.register(VisitedUrl)