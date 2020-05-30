from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .models import SiteService
from siteHomePage.forms import FeedbackForm, SnippetForm

def services(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
    form = FeedbackForm()
    services_list = SiteService.objects.order_by('-service_item_date')
    return render(request, 'siteServices/services.html', {'services_list': services_list,'form':form})

def service_detail(request, service_id):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
    form = FeedbackForm()
    try:
        a = SiteService.objects.get(id = service_id)
    except:
        raise Http404("Такой услуги не существует")
    return render(request, 'siteServices/one_service.html', {'service': a, 'form':form})

