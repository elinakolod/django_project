from django.http import HttpResponse
from django.shortcuts import redirect, render

from recipes.forms import RecipeForm
from .models import Recipe
from django.views.generic import ListView, DetailView, View

class IndexView(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'

class ShowView(DetailView):
    model = Recipe
    template_name = 'sandbox/show.html'
    context_object_name = 'recipe'

class NewView(View):
    template_name = 'recipes/new.html'
    form_class = RecipeForm

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect('foodie_app:show', category_id=recipe.category.id)
