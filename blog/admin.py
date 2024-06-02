from django.contrib import admin
from .models import Category, Post
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author',)
    search_fields = ('id', 'title', 'category__category_name',)
    list_editable = ('category',)


admin.site.register(Category)
admin.site.register(Post, BlogAdmin)

