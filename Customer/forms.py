from django import forms
from .models import customer

class customerForm(forms.ModelForm):
    
    class meta():
        
        model = customer
        fields = ('customer_count', 'table_number')
        lables = {'customer_count':"利用者人数", 'table_number':"テーブル番号"}
        
class AddCustomer(forms.ModelForm):
    class Meta():
        
        model = customer
        fileds = ('customer_count', 'table_number')
        lables = {'customer_count':"利用者人数", 'table_number':"テーブル番号"}
