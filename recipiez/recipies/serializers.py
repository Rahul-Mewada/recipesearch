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

class CreatableSlugRelatedField(serializers.SlugRelatedField):
    
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=data)
        except (TypeError, ValueError):
            self.fail('invalid')


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

class IngredientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=64)
    unit = serializers.CharField(max_length=32, allow_blank = True)
    
    class Meta:
        model = Ingredient
        fields = [
            'name',
            'unit',
            'quantity',
            'raw'
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


class RecipeSerialzer(serializers.ModelSerializer):
    url = VisitedUrlSerializer(many = False)
    author = AuthorSerializer(many = False)
    image = ImageSerializer(many = False)
    rating = RatingSerializer(many = False)
    keywords = KeywordSerializer(many = True)

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
    
