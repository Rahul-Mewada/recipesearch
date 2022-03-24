from django.db import models

# class Author(models.Model):
#     name = models.CharField(max_len = 64)
#     url = models.URLField()

#     def __str__(self):
#         return self.name
    
#     def __repr__(self):
#         return self.name

# class Image(models.Model):
#     height = models.IntegerField(blank = True)
#     width = models.IntegerField(blank = True)
#     caption = models.TextField(blank = True)
#     url = models.URLField()

#     def __str__(self):
#         return self.url
    
#     def __repr__(self):
#         return self.url

# class IngredientName(models.Model):
#     name = models.CharField(max_len = 64, db_index = True, unique = True)

# class IngredientUnit(models.Model):
#     unit = models.CharField(max_len = 32, db_index = True, unique = True)

# class Instruction(models.Model):
#     instruction = models.TextField()

# class Cuisine(models.Model):
#     cuisine = models.CharField(max_len = 64, db_index = True, unique = True)

# class Keyword(models.Model):
#     keyword = models.CharField(max_len = 64, db_index = True, unique = True)

# class Category(models.Model):
#     category = models.CharField(max_len = 64, db_index = True, unique = True)

class Recipe(models.Model):
    name = models.CharField(max_length=128)
    # image = models.OneToOneField(Image, blank = True)
    # author = models.OneToOneField(Author, blank = True)
    date_published = models.CharField(max_length = 32, blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    prep_time = models.CharField(max_length = 32, blank = True, null = True)
    cook_time = models.CharField(max_length = 32, blank = True, null = True)
    total_time = models.CharField(max_length = 32, blank = True, null = True)
    # keywords = models.ManyToManyRel(Keyword)
    servings = models.IntegerField(blank = True, null = True)
    # categories = models.ManyToManyRel(Category, blank = True)
    # cuisines = models.ManyToManyRel(Cuisine, blank = True)
    url = models.URLField(unique = True)
    url_hash = models.BigIntegerField(db_index = True)

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
