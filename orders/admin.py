from django.contrib import admin

from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0
    raw_id_fields = ['product']


@admin.register(OrderStatus)
class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderStatus._meta.fields]
    list_editable = ['is_active']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]
    # list_editable = ['status']


@admin.register(ProductInOrder)
class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]


