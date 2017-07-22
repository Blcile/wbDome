from django.shortcuts import render
from django.http import response
from django.views.generic.list import ListView
from .models import Wblog,WbImg

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'weibo_list'

    def get_queryset(self):
        weibo_list = Wblog.objects.all()
        return weibo_list



