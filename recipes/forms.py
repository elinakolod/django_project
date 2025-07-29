from django import forms
from foodie_app.models import Category
from recipes.models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients', 'instructions', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Recipe Title'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Description'}),
            'ingredients': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Ingredients'}),
            'instructions': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Instructions'}),
        }

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError("Category is required.")
        return category
