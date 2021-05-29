from django.urls import path
from .views import (HomeView,
                    ContactView,
                    ProductView,
                    CartView,
                    CheckoutView,
                    )
from .import views
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('ContactUs/', ContactView.as_view(), name='contact'),
    path('Product/', ProductView.as_view(), name='product'),
    path('Cart/', CartView.as_view(), name='cart'),
    path('Checkout/', CheckoutView.as_view(), name='checkout'),
    path('Login/', views.loginPage, name='login'),
    path('Register/', views.registerPage, name='register'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order')
]


