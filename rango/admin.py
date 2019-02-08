from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
<<<<<<< HEAD
admin.site.register(UserProfile)
=======
>>>>>>> 8d8518b9ba9a577219f0fa1b870c0ce9f85856a0
