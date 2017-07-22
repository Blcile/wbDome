from django.shortcuts import render
from django.http import response
from django.views.generic.list import ListView
from .models import Wblog,WbImg

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model=Wblog

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['wb_list'] = Wblog.objects.all()[:10]
        return context



