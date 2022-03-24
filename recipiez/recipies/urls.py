from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.RecipeDetailAPIView.as_view())
]