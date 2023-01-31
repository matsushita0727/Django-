from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App_Folder.urls')),
    path('', include('invoice.urls')),
    path('admin/', admin.site.urls),
    path('', include('stock.urls')),
    path('Home_Folder',include('Home_Folder.urls')),
    
]