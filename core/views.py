from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'Homepage/index.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'Homepage/contact.html')

class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'Homepage/products.html', context)
class CartView(View):
    def get(self, request):
        return render(request, 'Homepage/cart.html')

class LoginPage(View):
    def get(self, request):
        return render(request, 'Homepage/login.html')

class RegisterPage(View):
    def get(self, request):
        return render(request, 'Homepage/register.html')