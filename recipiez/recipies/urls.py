from django.urls import path
from . import views

#api/
urlpatterns = [
    path('recipies/<int:pk>', views.RecipeDetailAPIView.as_view()),
    path('recipies/', views.RecipeListAPIView.as_view()),
    path('recipies/add', views.RecipeAPIView.as_view()),
    path('urls/', views.get_url_view),
    path('urls/create', views.VisitedUrlCreateAPIView.as_view()),
    path('keywords/', views.KeywordListAPIView.as_view()),
    path('ingredients/', views.IngredientAPIView.as_view())
]