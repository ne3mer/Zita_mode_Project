from django.contrib import admin
from django.http import HttpRequest
from . import models

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)

    def save_model(self, request: HttpRequest, obj: Product, form, change):
        return super().save_model(request, obj, form, change)


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
