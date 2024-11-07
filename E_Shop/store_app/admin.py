from django.contrib import admin

# Register your models here.

from .models import  *

class ImagesTublerInline(admin.TabularInline): #to show the image in product model
    model = Images

class TagTublerInline(admin.TabularInline): #to show the tags in product model
    model = Tags

class ProductAdmin(admin.ModelAdmin): # implementing them here (image and tags)
    inlines = [ImagesTublerInline, TagTublerInline]

admin.site.register(Tags)
admin.site.register(Images)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product, ProductAdmin)

