from django.urls import path
from . import views

urlpatterns = [
    path("tyumon",views.tyumon,name="tyumon"),
    path("menyu",views.menyu,name="menyu"),
    path("zaiko",views.zaiko,name="zaiko"),
    path("qr",views.FormView.as_view(),name="qr"),
    path("qritiran",views.nippoListView,name="qritiran"),
    path("qrdelete/<int:id>",views.nippoDeleteView,name="qrdelete"),
    path("createQr",views.createQrView.as_view(),name="createQr"),
    path("reziList",views.kaikeiListView,name="reziList"),
    path("detail/<int:pk>/",views.kaikeiDetailView, name="kaikei-detail"),
    path("rezi/<int:pk>/",views.rezi, name="rezi"),
    path("home",views.home,name="home"),
    path("paypay",views.paypay,name="paypay"),
]