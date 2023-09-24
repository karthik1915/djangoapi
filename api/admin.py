from django.contrib import admin
from .models import Image, Post


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "category")
    list_filter = ("category",)  # Optional: Add filters
    search_fields = ("title", "category")  # Optional: Add search fields


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "authorname", "timestamp", "category", "tags")
    list_filter = ("timestamp", "category")
    search_fields = ("title", "authorname")
