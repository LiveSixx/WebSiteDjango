from django.shortcuts import render

from siteServices.models import SiteService
from .models import Advantage
from .forms import FeedbackForm, SnippetForm
from siteReviews.models import SnippetReview

def index(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()

    form = FeedbackForm()
    reviews_list_home_page = SnippetReview.objects.order_by('-time_pub_review')[:3]
    services_list_home_page = SiteService.objects.order_by('-service_item_title')[:4]
    advantage_list_home_page = Advantage.objects.order_by('-advantage_item_title_home_page')[:4]
    return render(request, 'siteHomePage/homePage.html', 
    {'services_list_home_page':services_list_home_page, 
    'advantage_list_home_page':advantage_list_home_page, 
    'form':form,
    'reviews_list_home_page':reviews_list_home_page})

def about(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()

    form = FeedbackForm()
    return render(request, 'siteHomePage/about.html',{'form':form})

def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()