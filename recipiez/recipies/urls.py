from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.RecipeDetailAPIView.as_view()),
    path('', views.RecipeListAPIView.as_view()),
    path('add', views.RecipeCreateAPIView.as_view())
]