from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from recipes.models import Recipe

def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'sandbox/index.html', context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'sandbox/index.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        filtered_recipes =  Recipe.objects.filter(category__name__iexact='Pizza')
        return filtered_recipes

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'sandbox/show.html'
    context_object_name = 'recipe'

class SpecificView(View):
    def get(self, request, *args, **kwargs):
        tasty_recipes = Recipe.objects.filter(description__icontains='tasty')
        context = {
            'recipes': tasty_recipes
        }
        return render(request, 'sandbox/tasty_recipes.html', context)
