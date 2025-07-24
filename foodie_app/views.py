from django.shortcuts import get_object_or_404, render
from foodie_app.models import Category
from recipes.models import Recipe
from django.views.generic import ListView, View, CreateView
from foodie_app.forms import CategoryForm

class IndexView(ListView):
    model = Category
    template_name = 'foodie_app/index.html'
    context_object_name = 'categories'

class ShowView(View):
    def get(self, request, *args, **kwargs):
        category_id = kwargs.get('category_id')
        recipes = Recipe.objects.filter(category=category_id)
        category = get_object_or_404(Category, id=category_id)
        context = {
            'recipes': recipes,
            'category': category,
        }
        return render(request, 'recipes/index.html', context)

class NewView(CreateView):
    template_name = 'foodie_app/new.html'
    success_url = '/'
    form_class = CategoryForm
