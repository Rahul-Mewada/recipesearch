from typing import List
from rest_framework import generics
from rest_framework.views import APIView
from .models import IngredientName, Recipe, VisitedUrl, Keyword, Ingredient
from .serializers import IngredientNameSerializer, IngredientSerializer, KeywordRecipeSerializer, KeywordSerializer, RecipeSerialzer, VisitedUrlSerializer,\
     RecipeViewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class RecipeDetailAPIView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerialzer
    lookup_field = 'pk'

class RecipeListAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeViewSerializer

class KeywordListAPIView(generics.ListAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordRecipeSerializer

class VisitedUrlCreateAPIView(generics.CreateAPIView):
    queryset = VisitedUrl.objects.all()
    serializer_class = VisitedUrlSerializer

class RecipeAPIView(APIView):
    def get(self, format=None):
        queryset = Recipe.objects.all()
        serializer = RecipeViewSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RecipeSerialzer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("Valid")
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=201)
        print("Not valid")
        return Response(status=400)

class IngredientAPIView(APIView):
    def get(self, format=None):
        queryset = Ingredient.objects.all()
        serializer = IngredientSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngredientSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=201)
        return Response(status=400)

@api_view(["GET"])
def get_url_view(request, *args, **kwargs):
    """
    Returns a list of all urls if no json provided
    else echos the existing url
    """
    if not request.data:
        queryset = VisitedUrl.objects.all()
        data = VisitedUrlSerializer(queryset, many=True).data
    else:
        url_hash = request.data['url_hash']
        url = request.data['url']
        queryset = VisitedUrl.objects.filter(url_hash=url_hash)\
            .filter(url=url)
        data = VisitedUrlSerializer(queryset, many=True).data
        if not data:
            return Response(data=[], status = 404)
    return Response(data, status = 200)

@api_view(["GET"])
def get_recipe_from_ingredient(request, *args, **kwargs):
    qs_ingredient_name = IngredientName.objects.filter(name__contains=request.data['name'])
    qs_ingredients = Ingredient.objects.filter(name__in = qs_ingredient_name)
    qs_recipies = Recipe.objects.filter(ingredients__in = qs_ingredients).distinct()
    serializer = RecipeViewSerializer(qs_recipies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_recipe_from_keyword(request, *args, **kwargs):
    qs_keywords = Keyword.objects.filter(keyword__contains = request.data['keyword']).distinct()
    qs_recipies = Recipe.objects.filter(keywords__in = qs_keywords).distinct()
    serializer = RecipeViewSerializer(qs_recipies, many=True)
    return Response(serializer.data)