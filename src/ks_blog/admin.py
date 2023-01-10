from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified', 'author', 'status')
    fieldsets = [
        (None, {'fields': [('title', 'body', )]}),
        ('Properties', {'fields': [('published', 'status')]}),
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
