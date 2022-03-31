from copy import copy
from urllib.parse import SplitResultBytes
from html5lib import serialize
from rest_framework import serializers, validators
from .models import Ingredient, IngredientName, IngredientUnit, Recipe, VisitedUrl, Author, Image, Rating, Keyword
from drf_writable_nested.mixins import UniqueFieldsMixin, NestedCreateMixin
from django.core.exceptions import ObjectDoesNotExist
class VisitedUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitedUrl
        fields = [
            'url',
            'url_hash'
        ]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'name',
            'url'
        ]

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'height',
            'width',
            'caption',
            'url'
        ]

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            'count',
            'value'
        ]

class KeywordSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = [
            'keyword'
        ]

class KeywordRecipeSerializer(serializers.ModelSerializer):
    recipies = serializers.StringRelatedField(many=True)
    class Meta:
        model = Keyword
        fields = [
            'keyword',
            'recipies'
        ]

class IngredientNameSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = IngredientName
        fields = [
            'name'
        ]

class IngredientUnitSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = IngredientUnit
        fields = [
            'unit'
        ]

class IngredientSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    name = serializers.CharField(max_length=64)
    unit = serializers.CharField(max_length=32, allow_blank = True)
    
    class Meta:
        model = Ingredient
        fields = [
            'name',
            'unit',
            'quantity',
            'raw',
            'recipe'
        ]

    def create(self, validated_data):
        name = validated_data.pop('name')
        unit = validated_data.pop('unit')
        ingredient_name, created = IngredientName.objects.get_or_create(name=name)
        ingredient_unit, created = IngredientUnit.objects.get_or_create(unit=unit)
        ingredient = Ingredient.objects.create(
            name = ingredient_name,
            unit = ingredient_unit,
            **validated_data
        )

class RecipeViewSerializer(serializers.ModelSerializer):
    url = VisitedUrlSerializer(many = False)
    author = AuthorSerializer(many = False)
    image = ImageSerializer(many = False)
    rating = RatingSerializer(many = False)
    keywords = KeywordSerializer(many = True)
    ingredients = IngredientSerializer(many = True)

    class Meta:
        model = Recipe
        fields = [
            'name',
            'image',
            'author',
            'date_published',
            'description',
            'keywords',
            'prep_time',
            'cook_time',
            'total_time',
            'ingredients',
            'servings',
            'url',
            'rating'
        ]

class RecipeSerialzer(NestedCreateMixin, serializers.ModelSerializer):
    url = VisitedUrlSerializer(many = False)
    author = AuthorSerializer(many = False)
    image = ImageSerializer(many = False)
    rating = RatingSerializer(many = False)
    keywords = KeywordSerializer(many = True)
    ingredients = serializers.ListField()

    class Meta:
        model = Recipe
        fields = [
            'name',
            'image',
            'author',
            'date_published',
            'description',
            'keywords',
            'prep_time',
            'cook_time',
            'total_time',
            'ingredients',
            'servings',
            'url',
            'rating'
        ]

    def create(self, validated_data):
        url_data = validated_data.pop('url')
        author_data = validated_data.pop('author')
        image_data = validated_data.pop('image')
        rating_data = validated_data.pop('rating')
        keyword_data = validated_data.pop('keywords')
        ingredient_data = validated_data.pop('ingredients')

        url = VisitedUrl.objects.create(**url_data)
        author = Author.objects.create(**author_data)
        image = Image.objects.create(**image_data)
        rating = Rating.objects.create(**rating_data)
        recipe = Recipe.objects.create(
            image = image,
            author = author,
            url = url,
            rating = rating, 
            **validated_data)

        for k in keyword_data:
            keyword, created = Keyword.objects.get_or_create(keyword=k['keyword'])
            recipe.keywords.add(keyword)
    
        for i in ingredient_data:
            name = i.pop('name')
            unit = i.pop('unit')

            if unit:
                ingredient_unit, created = IngredientUnit.objects.get_or_create(unit=unit)
            else:
                ingredient_unit = None

            ingredient_name, created = IngredientName.objects.get_or_create(
                name = name
            )

            ingredient = Ingredient.objects.create(
                name=ingredient_name,
                unit=ingredient_unit,
                recipe=recipe,
                **i
            )
            # recipe.ingredients.add(ingredient)
