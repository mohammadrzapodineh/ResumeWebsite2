from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from about.models import About, WhatIdo


class HomePage(TemplateView):
    template_name = 'home/index.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['whatdo_list'] = WhatIdo.objects.all()
        return context
    