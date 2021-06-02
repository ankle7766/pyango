from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request就是HttpResponse類型對象
# request包含瀏覽器的請求信息
def index(request):
    '''首頁'''
    return render(request, 'booktest/index.html')

def show_arg(request, num):
    return HttpResponse(num)

def login(request):
    '''顯示登陸頁面'''
    return render(request, 'booktest/login.html')

def login_check(request):
    '''登錄校驗試圖'''
    # 1.獲取提交的用戶名和密碼

    # 2.進行登錄的校驗

    # 3.返回應答