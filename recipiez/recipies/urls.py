from django.urls import path
from . import views

#api/
urlpatterns = [
    path('recipies/<int:pk>', views.RecipeDetailAPIView.as_view()),
    path('recipies/', views.RecipeListAPIView.as_view()),
    path('recipies/add', views.RecipeViewSet.as_view({'post' : 'list'})),
    path('urls/', views.get_url_view)
]