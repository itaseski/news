from django.contrib import admin

from .models import News, Category



class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'category')
    list_editable = ('is_published',)

admin.site.register(News, NewsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title', )    

admin.site.register(Category, CategoryAdmin)
