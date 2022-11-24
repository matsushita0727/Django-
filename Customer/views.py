from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from . import models

def customer(request):
    
    return render(request, 'App_Folder_HTML/CustomerTouroku.html')

def kakunin(request):
    
    return render(request, 'App_Folder_HTML/Kakunin.html')

def menu(request):
    
    return render(request, 'App_Folder_HTML/Menu.html')

class menuList(ListView):
    
    model = models.menu_list
    
    context_object_name = 'menu_list'
    
    template_name = "App_Folder_HTML\Menu_list.html"