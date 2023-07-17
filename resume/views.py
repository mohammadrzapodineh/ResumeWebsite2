from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Skill, Experience, Education


class ResumeView(TemplateView):
    template_name = 'resume/resume.html'
    
    
    def get_context_data(self, **kwargs):
        skills = Skill.objects.all()
        experinces = Experience.objects.all()
        educations = Education.objects.all()
        context = super().get_context_data(**kwargs)
        context['skills'] = skills
        context['experinces'] = experinces
        context['educations'] = educations
        return context