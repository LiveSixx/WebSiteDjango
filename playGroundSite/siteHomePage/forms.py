from django import forms
from .models import Snippet

class FeedbackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя','maxlength':'45'}))
    phone = forms.IntegerField(label='Phone',widget=forms.TextInput(attrs={'placeholder': 'Контактный телефон','maxlength':'45'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Вопрос (максимум 250 символов)','maxlength':'250'}))

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name', 'phone', 'body')