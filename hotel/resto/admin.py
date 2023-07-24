from django.contrib import admin

from resto.models import Category,Product
class Categoryadmin(admin.ModelAdmin):
    list_display =['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,Categoryadmin)
class Productadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product,Productadmin)
