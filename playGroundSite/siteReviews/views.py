from django.shortcuts import render
from siteHomePage.forms import FeedbackForm, SnippetForm

from .forms import SnippetReviewForm, ReviewForm

from .models import SnippetReview

def reviews(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()

    form = FeedbackForm()
    
    if request.method == 'POST':
        formReview = SnippetReviewForm(request.POST)
        if formReview.is_valid():
            formReview.save()

    formReview = ReviewForm()
    
    reviews_list = SnippetReview.objects.order_by('-time_pub_review')
    return render(request, 'siteReviews/reviews.html', {'form':form, 'formReview':formReview, 'reviews_list':reviews_list})
