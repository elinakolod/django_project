from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'

class ShowView(DetailView):
    model = Recipe
    template_name = 'sandbox/show.html'
    context_object_name = 'recipe'
