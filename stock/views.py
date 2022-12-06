from msilib.schema import ListView
from django.shortcuts import render



# Create your views here.

from .filters import 作成したフィルター

class obj(ListView):
    ...

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["filter"] = 作成したフィルター(self.request.GET, queryset=self.get_queryset())
        return ctx