from django.contrib import admin

from .models import Comment,Content


@admin.register(Content)

class ContentAdmin(admin.ModelAdmin):

    list_display = ['title','slug','author','publish','status']
    list_filter = ['created','publish','status','author']
    search_fields = ['title','body']
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status','publish']


@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','content','created','active']
    list_filter = ['active','created','updated']
    search_fields = ['body','email','name']