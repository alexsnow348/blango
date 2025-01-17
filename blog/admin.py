from django.contrib import admin
from blog.models import Tag, Post, Comment
# Register your models here.
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')
    list_display = ('summary', 'content')

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)