from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App_Folder.urls')),
    path('', include('invoice.urls')),
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('', include('stock.urls')),
    path('Home_Folder',include('Home_Folder.urls')),
    
=======
    path('Home_Folder', include('Home_Folder.urls')),

>>>>>>> 3a6c72a46c0691139db8d1e362061da0a9103511
]