from django.contrib import admin

from .models import QrUrl
@admin.register(QrUrl)
class TestAdmin(admin.ModelAdmin):
    list_display = ['tableNumber','id']
