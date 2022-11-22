from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    path('site-header', views.site_header_partial, name='site_header_partial'),
    path('site-footer', views.site_footer_partial, name='site_footer_partial'),

]
