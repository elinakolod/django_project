from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.ShowView.as_view(), name='show'),
    path('new/', views.NewView.as_view(), name='new'),
]
