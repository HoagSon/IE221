from django.urls import path
from .views import (HomeView,
                    ContactView,
                    ProductView,
                    CartView,
                    CheckoutView,
                    LoginPage,
                    RegisterPage)
from .import views
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('ContactUs/', ContactView.as_view(), name='contact'),
    path('Product/', ProductView.as_view(), name='product'),
    path('Cart/', CartView.as_view(), name='cart'),
    path('Checkout/', CheckoutView.as_view(), name='checkout'),
    path('Login/', LoginPage.as_view(), name='login'),
    path('Register/', RegisterPage.as_view(), name='register'),
    path('update_item', views.updateItem, name='checkout')
]


