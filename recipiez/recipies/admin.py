from django.contrib import admin
from .models import IngredientName, IngredientUnit, Recipe, VisitedUrl, Image, Author, Rating, Keyword, Ingredient
# Register your models here.

admin.site.register(Recipe)
admin.site.register(VisitedUrl)
admin.site.register(Author)
admin.site.register(Image)
admin.site.register(Rating)
admin.site.register(Keyword)
admin.site.register(Ingredient)
admin.site.register(IngredientName)
admin.site.register(IngredientUnit)