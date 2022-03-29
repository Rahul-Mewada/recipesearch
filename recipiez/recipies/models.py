from ast import keyword
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django import urls
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

class Image(models.Model):
    height = models.IntegerField(blank = True, null = True)
    width = models.IntegerField(blank = True, null = True)
    caption = models.TextField(blank = True, null = True)
    url = models.URLField(max_length=400)

    def __str__(self):
        return self.url
    
    def __repr__(self):
        return self.url

# class IngredientName(models.Model):
#     name = models.CharField(max_len = 64, db_index = True, unique = True)

# class IngredientUnit(models.Model):
#     unit = models.CharField(max_len = 32, db_index = True, unique = True)

# class Instruction(models.Model):
#     instruction = models.TextField()

# class Cuisine(models.Model):
#     cuisine = models.CharField(max_len = 64, db_index = True, unique = True)

class Keyword(models.Model):
    keyword = models.CharField(max_length = 64, db_index = True, unique = True)

    def __str__(self):
        return self.keyword

# class Category(models.Model):
#     category = models.CharField(max_len = 64, db_index = True, unique = True)

class VisitedUrl(models.Model):
    url = models.URLField(max_length=400)
    url_hash = models.BigIntegerField(db_index = True)

    def __str__(self):
        return self.url

class Rating(models.Model):
    count = models.IntegerField()
    value = models.FloatField()

    def __str__(self):
        return str(self.value)

class Recipe(models.Model):
    name = models.CharField(max_length=128)
    image = models.OneToOneField(Image, on_delete=models.CASCADE,\
         blank = True, null = True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE,\
        blank = True, null = True)
    date_published = models.CharField(max_length = 32, blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    prep_time = models.CharField(max_length = 32, blank = True, null = True)
    cook_time = models.CharField(max_length = 32, blank = True, null = True)
    total_time = models.CharField(max_length = 32, blank = True, null = True)
    keywords = models.ManyToManyField(Keyword, related_name='recipies')
    servings = models.CharField(max_length = 32, blank = True, null = True)
    # categories = models.ManyToManyRel(Category, blank = True)
    # cuisines = models.ManyToManyRel(Cuisine, blank = True)
    url = models.OneToOneField(VisitedUrl, on_delete=models.CASCADE, unique=True)
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE, unique = True, \
        blank=True, null=True)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

# class RecipeInstructions(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, db_index = True)
#     instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE, db_index = True)
#     step = models.IntegerField()

#     class Meta:
#         unique_together = [['recipe', 'instruction']]

# class RecipeIngredients(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, db_index = True)
#     ingredient_name = models.ForeignKey(IngredientName, on_delete=models.CASCADE, db_index = True)
#     ingredient_quantity = models.DecimalField()
#     ingredient_unit = models.ForeignKey(IngredientUnit, on_delete=models.CASCADE)
#     ingredient_raw = models.CharField(100)

#     class Meta:
#         unique_together = [['recipe', 'ingredient_raw']]
