from django.contrib import admin

from blog.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'category')
    search_fields = ['id', 'name', 'content']
    list_filter = ['status', 'category', 'created_at']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)