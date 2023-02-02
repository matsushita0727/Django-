from asyncio import create_subprocess_exec
from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
from . import graph

# Create your views here.

'''from .filters import 作成したフィルター

class obj(ListView):
    ...
    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["filter"] = 作成したフィルター(self.request.GET, queryset=self.get_queryset())
        return ctx'''

class Index(TemplateView):

    #テンプレートファイル連携
    template_name = "Index.html"

    #変数としてグラフイメージをテンプレートに渡す
    def get_context_data(self, **kwargs):

        #グラフオブジェクト
        qs    = models.stock.objects.all()  #モデルクラス(ProductAテーブル)読込
        x     = [x.created_at for x in qs]           #X軸データ
        y     = [y.inventory for y in qs]        #Y軸データ
        chart = graph.Plot_Graph(x,y)          #グラフ作成

        #変数を渡す
        context = super().get_context_data(**kwargs)
        context['chart'] = chart
        return context

    #get処理
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
