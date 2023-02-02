from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from PIL import Image
import qrcode   # pip install qrcode, pillow
import base64
from io import BytesIO
from . import forms
from .forms import qrNumber
from django.views.generic import TemplateView
from .models import QrUrl
from invoice.models import Invoice
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
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




class createQrView(TemplateView):
    def get(form2,request):
        form2 =forms.qrNumber()
        ctx = {}
        ctx["form2"] = form2
        return render(request, "Home_Folder_HTML/creteQr.html",ctx)
    def post(form2,request,):
        form2 = forms.qrNumber(request.POST or None)
        if request.method == "POST" and form2.is_valid():
            idf = form2.cleaned_data["number"]
            try:
                id = QrUrl.objects.get(pk=idf)
            except QrUrl.DoesNotExist:
                return False
            table = QrUrl.objects.values_list('tableNumber',flat=True).get(pk=idf)
            img = qrcode.make("https://127.0.0.1:8000"+"?"+str(id)+"&"+str(table))
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            qr = base64.b64encode(buffer.getvalue()).decode().replace("'", "")
            param = { 'qr': qr}
        return render(request,'Home_Folder_HTML/hakouQr.html',param)


def nippoListView(request):
    template_name = "Home_Folder_HTML/qritiran.html"
    ctx = {}
    qs = QrUrl.objects.all()
    ctx["object_list"] = qs

    return render(request, template_name, ctx)


def nippoDeleteView(request, id):
    template_name = "Home_Folder_HTML/qrdelete.html"
    obj = get_object_or_404(QrUrl, pk=id)
    ctx = {"object": obj}
    if request.POST:
        obj.delete()
        return redirect("home")
    return render(request, template_name, ctx)

def kaikeiListView(request):
    template_name = "Home_Folder_HTML/reziList.html"
    ctx = {}
    qs = Invoice.objects.all()
    ctx["object_list"] = qs

    return render(request, template_name, ctx)

def kaikeiDetailView(request,pk):
    template_name = "Home_Folder_HTML/rezi.html"
    ctx = {}
    q = Invoice.objects.get(pk=pk)
    ctx["object"] = q
    return render(request, template_name,ctx)

def rezi(request,pk):
    template_name = "Home_Folder_HTML/rezi.html"
    obj = get_object_or_404(Invoice, pk=pk)
    ctx = {"object": obj}
    return render(request, template_name,ctx)

def kaikei(request):
    return render(request,'Home_Folder_HTML/kaikei.html')

def home(request):
    return render(request, 'App_Folder_HTML/home.html')


def paypay(request):
    return render(request, 'Home_Folder_HTML/paypay.html')