from django.shortcuts import render

def index(request):
    return render(request, 'siteHomePage/homePage.html')

def about(request):
    return render(request, 'siteHomePage/about.html')