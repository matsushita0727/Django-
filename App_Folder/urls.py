from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountRegistration.as_view(), name='register'),
]