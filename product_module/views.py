from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from product_module.models import Product


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product
