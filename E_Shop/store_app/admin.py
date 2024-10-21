from django.contrib import admin

# Register your models here.

from .models import  *

class ImagesTublerInline(admin.TabularInline):
    model = Images

class TagTublerInline(admin.TabularInline):
    model = Tags

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTublerInline, TagTublerInline]

admin.site.register(Tags)
admin.site.register(Images)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product, ProductAdmin)

