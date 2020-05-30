from django.contrib import admin

from .models import Advantage, Snippet

admin.site.register(Advantage)
#admin.site.register(Snippet)

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'body')