from django.contrib import admin
from blog_api.models import Post, Comment, Category, PostImages

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(PostImages)