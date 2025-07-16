from django.http import HttpResponse
from django.shortcuts import render

def recipes(request):
    return HttpResponse("This is the recipes page.")
