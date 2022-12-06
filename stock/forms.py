

from django import forms
import stock


class AddStock(forms.ModelForm):
    class Meta():
        
        model = stock
        fileds = ('customer_count', 'table_number')
        lables = {'customer_count':"利用者人数", 'table_number':"テーブル番号"}
