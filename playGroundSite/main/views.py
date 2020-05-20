from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/homePage.html')

def mainpage(request):
    return HttpResponse("<h2>Main Page!</h2>")

def contact(request):
    return render(request, 'main/basic.html', {'contact':['Некоторый текст из кортежа с массивом 1', 
    'Некоторый текст из кортежа с массивом 2', 
    'LiveSixx']})

