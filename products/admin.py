from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    # list_editable = ['is_active']
    inlines = [ProductImageInline]


@admin.register(CountryOfOrigin)
class CountryOfOriginAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CountryOfOrigin._meta.fields]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Language._meta.fields]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Author._meta.fields]
    inlines = [ProductInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Genre._meta.fields]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]
    list_editable = ['is_active', 'is_main']


