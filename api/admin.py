from django.contrib import admin

from posts.models import Follow, Post

admin.site.register(Post)
admin.site.register(Follow)
