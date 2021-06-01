from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from .models import *
import json
import datetime
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .utils import cookieCart
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            cookieData = cookieCart(request)
            cartItems = cookieData['cartItems']
        context = {'cartItems': cartItems}
        return render(request, 'Homepage/index.html', context)

class ContactView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            cookieData = cookieCart(request)
            cartItems = cookieData['cartItems']
        context = {'cartItems': cartItems}
        return render(request, 'Homepage/contact.html', context)

class ProductView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            cookieData = cookieCart(request)
            cartItems = cookieData['cartItems']
        products = Product.objects.all()
        context = {'products': products, 'cartItems': cartItems}
        return render(request, 'Homepage/products.html', context)
class CartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            cookieData = cookieCart(request)
            cartItems = cookieData['cartItems']
            order = cookieData['order']
            items = cookieData['items']
        context = {'items': items, 'order': order, 'cartItems': cartItems}
        return render(request, 'Homepage/cart.html', context)

class CheckoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            cookieData = cookieCart(request)
            cartItems = cookieData['cartItems']
            order = cookieData['order']
            items = cookieData['items']
        context = {'items': items, 'order': order, 'cartItems': cartItems}
        return render(request, 'Homepage/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productID = data['productId']
    action = data['action']

    print('Action:', action)
    print('ProductID:', productID)

    customer = request.user.customer
    product = Product.objects.get(id=productID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        print('User not logged in...')
        print('COOKIES:', request.COOKIES)
        name = data['form']['name']
        email = data['form']['email']

        cookieData = cookieCart(request)
        items = cookieData['items']
        customer, created = Customer.objects.get_or_create(
            email=email,
        )
        customer.name = name
        customer.save()

        order = Order.objects.create(
            customer=customer,
            complete=False,
        )

        for item in items:
            print((item))
            product = Product.objects.get(id=item['product']['id'])
            orderItem = OrderItem.objects.create(
                product=product,
                order=order,
                quantity=item['quantity']
            )
    total = data['form']['total']
    order.transaction_id = transaction_id
    order.complete = True

    if total == order.get_cart_total:
        order.complete = True
    order.save()
    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        phone=data['shipping']['phone']
    )
    return JsonResponse('Payment complete', safe=False)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Customer.objects.create(
                user=user,
                name=username,
                email=form.cleaned_data.get('email')
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'Homepage/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        context = {}
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, 'Homepage/login.html', context)
        return render(request, 'Homepage/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')