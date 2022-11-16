from django.shortcuts import render
from django.urls import reverse

def customer(request):
    
    return render(request, 'App_Folder_HTML/CustomerTouroku.html')

def kakunin(request):
    
    return render(request, 'App_Folder_HTML/Kakunin.html')

def menu(request):
    
    return render(request, 'App_Folder_HTML/Menu.html')