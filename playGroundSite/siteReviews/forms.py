from django import forms
from .models import SnippetReview

class ReviewForm(forms.Form):
    name_review = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя','maxlength':'45'}))
    email_review = forms.EmailField(label='E-mail',widget=forms.TextInput(attrs={'placeholder': 'Почта','maxlength':'45'}))
    body_review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Отзыв','maxlength':'400'}))

class SnippetReviewForm(forms.ModelForm):

    class Meta:
        model = SnippetReview
        fields = ('name_review', 'email_review', 'body_review')