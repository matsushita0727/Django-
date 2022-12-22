from django import forms
from .models import QrUrl

class tableNumber(forms.ModelForm):
    class Meta():
        model = QrUrl
        fields = ('tableNumber',)
        labels = {'tableNumber':'卓番'}

class qrNumber(forms.Form):
    number = forms.IntegerField(label= "卓番選択")
