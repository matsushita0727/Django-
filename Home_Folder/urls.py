from django.urls import path
from . import views

urlpatterns = [
    path("tyumon",views.tyumon,name="tyumon"),
    path("menyu",views.menyu,name="menyu"),
    path("zaiko",views.zaiko,name="zaiko"),
    path("qr",views.FormView.as_view(),name="qr"),
    path("table",views.table,name="table"),
    path("createQr",views.createQrView.as_view(),name="createQr"),
    path("kaikei",views.kaikei,name="kaikei"),
    path("home",views.home,name="home"),
    path("paypay",views.paypay,name="paypay"),
]