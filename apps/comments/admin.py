from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'message', 'name', 'email', 'rating',
                    'created_at')
    list_display_links = list_display


