from django.shortcuts import render

# Create your views here.

def index(request):
    '''首頁'''
    return render(request, 'booktest/index.html')