from django.contrib import admin

from . models import customer
from . models import menu_list

admin.site.register(customer)
admin.site.register(menu_list)
