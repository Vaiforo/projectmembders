from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterUserForm
from .models import *


class PMUserAdmin(UserAdmin):
    add_form = RegisterUserForm
    model = PMUser
    list_display = ['email', 'username', 'warns', 'banned']
    list_editable = ('banned',)


admin.site.register(PMUser, PMUserAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'content', 'is_published')
    # list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'cats')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Card, CardAdmin)
