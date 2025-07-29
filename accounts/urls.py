from django.urls import include, path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),  # Includes login, logout, password management URLs
]
