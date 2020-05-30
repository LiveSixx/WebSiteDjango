from django.contrib import admin

from .models import SnippetReview

@admin.register(SnippetReview)
class SnippetReviewAdmin(admin.ModelAdmin):
    list_display = ('name_review', 'email_review', 'body_review')
