from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from product_module.models import Product, ProductGallery


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        loaded_product = self.object
        context['product_gallery'] = ProductGallery.objects.filter(product_id=loaded_product.id).all()
        return context
