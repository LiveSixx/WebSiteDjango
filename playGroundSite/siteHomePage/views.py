from django.shortcuts import render

def index(request):
    return render(request, 'siteHomePage/homePage.html')

def homepage(request):
    return render(request, 'siteHomePage/homePage2.html')
