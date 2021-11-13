from django.contrib import admin
from blog.models import Post, BlogComment

admin.site.register(BlogComment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    class Media:
        js = ('tinyInject.js',)
