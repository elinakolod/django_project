from django.shortcuts import render

def index(request):
    data = {
        'message': 'Welcome to the Foodie app!',
        'items': ['Pizza', 'Burger', 'Sushi', 'Pasta']
    }
    context = {
        'foods': data['items'],
    }
    return render(request, 'sandbox/index.html', context)
