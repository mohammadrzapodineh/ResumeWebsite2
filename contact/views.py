from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm
from django.conf import settings
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages


class ContactPage(FormView):
    template_name = 'contact/contact_me.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact_me')
    
    
    
    def form_valid(self, form):
        '''
        When Form is Valid Send The Message Of User To Admins
        '''
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        email = form.cleaned_data['email']
        total_message = f"Hi Admin You Have one Mail Form name:{name}-Email:{email} And message is {message}"
        recipient_list = [admin[1] for admin in settings.ADMINS]
        send_mail("Message Form Your Resume Website", message=total_message, recipient_list=recipient_list,from_email=settings.DEFAULT_FROM_EMAIL)
        messages.success(self.request, 'Your Message Has Sent Success')
        return super().form_valid(form)