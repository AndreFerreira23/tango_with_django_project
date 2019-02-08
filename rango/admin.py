from django.contrib import admin
from rango.models import Category, Page

<<<<<<< HEAD
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
=======

admin.site.register(Category)
admin.site.register(Page)
>>>>>>> 08e4aa365923dc148f3d3e831e53be31ce129029
