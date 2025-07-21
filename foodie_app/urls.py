from django.urls import path
from . import views

app_name = 'foodie_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('recipes/<int:category_id>/', views.ShowView.as_view(), name='show'),
]
