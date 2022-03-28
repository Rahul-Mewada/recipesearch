from django.contrib import admin
from .models import Recipe, VisitedUrl, Image, Author, Rating
# Register your models here.

admin.site.register(Recipe)
admin.site.register(VisitedUrl)
admin.site.register(Author)
admin.site.register(Image)
admin.site.register(Rating)