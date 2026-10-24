from django.contrib import admin
from .models import product


@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('is_available', 'created_at')
