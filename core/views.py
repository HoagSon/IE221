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
        context = {'products':products}
        return render(request, 'Homepage/products.html', context)
class CartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}

        context = {'items': items, 'order': order}
        return render(request, 'Homepage/cart.html', context)

class CheckoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}

        context = {'items': items, 'order': order}
        return render(request, 'Homepage/checkout.html', context)

class LoginPage(View):
    def get(self, request):
        render(request, 'Homepage/login.html')

class RegisterPage(View):
    def get(self, request):
        render(request, 'Homepage/register.html')