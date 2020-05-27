from django.shortcuts import render

def reviews(request):
    return render(request, 'siteReviews/reviews.html')
