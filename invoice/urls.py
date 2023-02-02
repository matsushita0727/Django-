from django.urls import path

from invoice import views



urlpatterns = [
    path('itiran', views.InvoiceFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', views.InvoiceDetailView.as_view(), name='detail'),
     path('detail2/<int:pk>/', views.InvoiceDetailView2.as_view(), name='detail2'),
    path('create/', views.InvoiceCreateView.as_view(), name='create'),
    path('create2/', views.InvoiceCreateView2.as_view(), name='create2'),
    path('update/<int:pk>/', views.InvoiceUpdateView.as_view(), name='update'),
    path('update2/<int:pk>/', views.InvoiceUpdateView2.as_view(), name='update2'),
    path('delete/<int:pk>/', views.InvoiceDeleteView.as_view(), name='delete'),
    path('invoice_kaikei',views.invoiceK,name="invoice_kaikei"),
]

## クラスベースビューの場合
##path(URL, views.クラス名.as_view(), name=URL名称)

# 関数ベースビューの場合
##path(URL, views.関数名, name=URL名称)

#<int:pk>とはURL のその部分を、その名前のパラメーターとしてビューに渡します。
# 次に、ビュー関数を次のように記述できます。
#def my_view(request, pk):
#    ...
#ビュー内でその変数を参照します。
#通常、モデルの主キーを参照するために使用されます。