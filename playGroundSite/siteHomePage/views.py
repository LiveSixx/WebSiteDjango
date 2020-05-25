from django.shortcuts import render

def index(request):
    return render(request, 'siteHomePage/homePage.html')

def services(request):
    return render(request, 'siteHomePage/services.html')
