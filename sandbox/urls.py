from django.urls import path
from . import views

app_name = 'sandbox'
urlpatterns = [
    path('', views.index),
    path('foods/', views.RecipeListView.as_view(), name='food_list'),
    path('foods/<int:pk>', views.RecipeDetailView.as_view(), name='food_details'),
    path('tasty', views.SpecificView.as_view(), name='tasty_recipes'),
]
