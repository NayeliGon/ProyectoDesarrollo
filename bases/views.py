from django.shortcuts import render

from django.views import generic

class home(generic.TemplateView):
    template_name='base/base.html'