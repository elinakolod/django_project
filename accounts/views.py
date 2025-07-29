from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import pdb;

class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        #pdb.set_trace()
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('foodie_app:index')  # Redirect to the index page after registration
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
