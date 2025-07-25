from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View

from recipes.models import Recipe
from sandbox.forms import FeedbackForm
from sandbox.models import Feedback

def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'sandbox/index.html', context)

def thank_you(request):
    return HttpResponse("Thank you for your feedback!")

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                comment=form.cleaned_data['comment'],
                satisfaction=form.cleaned_data['satisfaction']
            )
            return redirect('sandbox:thank_you')
    else:
        form = FeedbackForm()
    context = {
        'form': form
    }
    return render(request, 'sandbox/feedback_form.html', context)

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
