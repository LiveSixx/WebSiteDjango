from django.shortcuts import render
from siteHomePage.forms import FeedbackForm, SnippetForm

def about(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
    form = FeedbackForm()
    return render(request, 'siteAbout/about.html',{'form':form})
