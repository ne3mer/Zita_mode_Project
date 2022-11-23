from django.shortcuts import render
from django.views.generic import ListView

from about_module.models import AboutMe


# Create your views here.


class AboutUsView(ListView):
    template_name = 'about_module/about_us.html'
    model = AboutMe
    context_object_name = 'about_us'
