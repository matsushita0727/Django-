from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App_Folder.urls')),
    path('customer/', include('Customer.urls')),
    path('', include('invoice.urls')),
    
]