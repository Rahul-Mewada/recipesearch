from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import Recipe, VisitedUrl, Image, Author, Rating, Keyword
from .serializers import KeywordSerializer, RecipeSerialzer, VisitedUrlSerializer,\
    ImageSerializer, AuthorSerializer, RatingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_writable_nested.mixins import UniqueFieldsMixin, NestedCreateMixin
class RecipeDetailAPIView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerialzer
    lookup_field = 'pk'

class RecipeListAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerialzer

class KeywordListAPIView(generics.ListAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class RecipeAPIView(APIView):
    def get(self, format=None):
        queryset = Recipe.objects.all()
        serializer = RecipeSerialzer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RecipeSerialzer(data=request.data)
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
