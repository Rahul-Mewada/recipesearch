from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import Recipe, VisitedUrl, Image, Author, Rating, Keyword
from .serializers import RecipeSerialzer, VisitedUrlSerializer,\
    ImageSerializer, AuthorSerializer, RatingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class RecipeDetailAPIView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerialzer
    lookup_field = 'pk'

class RecipeListAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerialzer

# class RecipeViewSet(viewsets.ModelViewSet):
#     serializer_class = RecipeSerialzer

#     def get_queryset(self):
#         return Recipe.objects.all()

#     def create(self, request, *args, **kwargs):
#         recipe_data = request.data
#         url_data = request.data["url"]
#         image_data  = request.data["image"]
#         author_data = request.data["author"]
#         rating_data = request.data["rating"]

#         url_instance = VisitedUrl.objects.create(
#             url = url_data["url"],
#             url_hash = url_data["url_hash"]
#         )

#         image_instance = Image.objects.create(
#             height = image_data["height"],
#             width = image_data["width"],
#             caption = image_data["caption"],
#             url = image_data["url"]
#         )
#         author_instance = Author.objects.create(
#             name = author_data["name"],
#             url = author_data["url"]
#         )

#         rating_instance = Rating.objects.create(
#             count = rating_data["count"],
#             value = rating_data["value"]
#         )

#         recipe_instance = Recipe.objects.create(
#             name = recipe_data["name"],
#             image = image_instance,
#             author = author_instance,
#             date_published = recipe_data["date_published"],
#             description = recipe_data["description"],
#             prep_time = recipe_data["prep_time"],
#             cook_time = recipe_data["cook_time"],
#             total_time = recipe_data["total_time"],
#             servings = recipe_data["servings"],
#             url = url_instance,
#             rating = rating_instance
#         )

#         url_instance.save()
#         image_instance.save()
#         author_instance.save()
#         recipe_instance.save()
#         rating_instance.save() 

#         serializer = RecipeSerialzer(recipe_instance)
#         return Response(serializer.data)

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
