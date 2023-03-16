from django.contrib import admin

from .models import *


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'content', 'is_published')
    # list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'cats')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Card, CardAdmin)
