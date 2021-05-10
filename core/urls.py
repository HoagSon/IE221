from django.urls import path
from .views import (HomeView, ContactView, ProductView)

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('ContactUs/', ContactView.as_view(), name='contact'),
    path('Product/', ProductView.as_view(), name='product')
]


