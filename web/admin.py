from django.contrib import admin
from web.models import Category,Product

admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display =  ("title","description")
admin.site.register(Product,ProductAdmin)