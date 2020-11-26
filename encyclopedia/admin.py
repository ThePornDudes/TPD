from django.contrib import admin

from .models import Wiki, edit_page

admin.site.register(Wiki)
admin.site.register(edit_page)
