from django.contrib import admin

from blog.models import Blog


# admin.site.register(Category)
#admin.site.register(Product)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
