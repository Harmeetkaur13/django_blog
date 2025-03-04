from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Comment, Post


# register it with a decorator
# ans then add the class which gives admin panel greater functionality and clarity
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.

# delete the existing Post model registration
# admin.site.register(Post)
admin.site.register(Comment)
