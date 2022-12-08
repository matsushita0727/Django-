from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from PIL import Image
import qrcode   # pip install qrcode, pillow
import base64
from io import BytesIO
from . import forms
from django.views.generic import TemplateView
from .models import QrUrl
# Create your views here.



def tyumon(request):
    return render(request, 'Home_Folder_HTML/tyumon.html')

def menyu(request):
    return render(request,'Home_Folder_HTML/menyu.html')

def zaiko(request):
    return render(request,'Home_Folder_HTML/zaiko.html')


class FormView(TemplateView):
    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                        "form":forms.tableNumber(),
        }
    def get(self,request):
        return render(request, "Home_Folder_HTML/qr.html",context=self.params)

    def post(self,request):
        if request.method == "POST":
            self.params["form"] =forms.tableNumber(request.POST)

            if self.params["form"].is_valid():
                self.params["form"].save(commit=True)
                self.params["Message"] = "入力情報が送信されました。"
        return render(request, "Home_Folder_HTML/qr.html",context=self.params)


def table(request):
    ctx = {}
    qr = QrUrl.objects.all()
    ctx["object_list"] = qr
    return render(request, "Home_Folder_HTML/qr.html", ctx)
class createQrView(TemplateView):
    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                        "form":forms.qrNumber(),
        }
    def get(self,request):
        #qrnumber = QrUrl.objects.get(tableNumber=1)
        id = QrUrl.objects.get(pk=1)
        img = qrcode.make("https://127.0.0.1:8000/"+"&"+str(id))
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr = base64.b64encode(buffer.getvalue()).decode().replace("'", "")
        param = { 'qr': qr}
        return render(request,'Home_Folder_HTML/creteQr.html',param)

def kaikei(request):
    return render(request,'Home_Folder_HTML/kaikei.html')

def home(request):
    return render(request, 'App_Folder_HTML/home.html')


def paypay(request):
    return render(request, 'Home_Folder_HTML/paypay.html')