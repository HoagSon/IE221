from django.shortcuts import render
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'Homepage/index.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'Homepage/contact.html')

class ProductView(View):
    def get(self, request):
        return render(request, 'Homepage/products.html')