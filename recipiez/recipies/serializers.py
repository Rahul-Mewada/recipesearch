from html5lib import serialize


from rest_framework import serializers
from .models import Recipe, VisitedUrl

class RecipeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'name',
            'date_published',
            'description',
            'prep_time',
            'cook_time',
            'total_time',
            'servings',
            'url'
        ]
        depth = 1

class VisitedUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitedUrl
        fields = [
            'url',
            'url_hash'
        ]