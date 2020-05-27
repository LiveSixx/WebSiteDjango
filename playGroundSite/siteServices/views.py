from django.shortcuts import render

def oneService(request):
    return render(request, 'siteServices/one_service.html')

def services(request):
    return render(request, 'siteServices/services.html')
