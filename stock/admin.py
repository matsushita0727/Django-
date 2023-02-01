from django.contrib import admin

# Register your models here.
from .models import stock

class TestProxy(stock):
    def __str__(self):
        return "TestProxy"

@admin.register(stock)
class TestAdmin(admin.ModelAdmin):
    ordering = ['category']
    list_display = ['category', 'item_name', 'inventory','created_at']
    ordering = ('-created_at',)
    list_filter = ["category"]
    search_fields = ['item_name']
