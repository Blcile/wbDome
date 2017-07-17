from django.shortcuts import render
from django.http import response
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_weibo_list'

    def get_queryset(self):
        """ return """
        return []
