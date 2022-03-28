from django.contrib import admin
from .models import Recipe, VisitedUrl, Image, Author
# Register your models here.

admin.site.register(Recipe)
admin.site.register(VisitedUrl)
admin.site.register(Author)
admin.site.register(Image)