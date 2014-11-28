from django.contrib import admin
from redirect.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'short_url',
        'android',
        'ios',
        'other',
    )

admin.site.register(Page, PageAdmin)