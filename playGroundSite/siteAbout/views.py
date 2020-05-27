from django.shortcuts import render

def about(request):
    return render(request, 'siteAbout/about.html')
