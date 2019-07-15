from django.contrib import admin
from .models import Post, Rubric

# Register your models here.
admin.site.register(Rubric)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'rubric',
                        'status')

    list_filter = ('status', 'created', 'publish', 'rubric')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

