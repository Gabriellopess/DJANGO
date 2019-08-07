from django.contrib import admin

# Register your models here.
from posts.models import post
admin.site.register(post)
