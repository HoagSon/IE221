from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(Request):
    response = HttpResponse()
    response.writelines("<h1>xin chao</h1>")
    response.write("Day la app home")
    return response
