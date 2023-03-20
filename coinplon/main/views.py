from django.shortcuts import render
from .functions import mutiplicate_by_5

def home_page(request):
    return render(request, 'main/home_page.html')

def about(request):
    # import pudb; pu.db()
    return render(request, 'main/about.html')
