from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Product, Profile, Gallery


class LandingView(TemplateView):
    template_name = "landing.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['profiles'] = Profile.objects.all()
        context['galleries'] = Gallery.objects.prefetch_related('images').all()
        return context
