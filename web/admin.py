from django.contrib import admin
from web.models import Category,Product,Price

admin.site.register(Category)
admin.site.register(Price)


class ProductAdmin(admin.ModelAdmin):
    list_display =  ("id","title","description")
admin.site.register(Product,ProductAdmin)