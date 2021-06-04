from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
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
    # request.POST 保存的是POST方式的提交參數 QueryDict
    # request.GET 保存的是GET方式的提交參數

    # 1.獲取提交的用戶名和密碼
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2.進行登錄的校驗
    # 實際開發時:根據用戶明和密碼查找數據庫
    # 模擬: ankle 123
    if username == 'ankle' and password == '123':
        # 用戶明和密碼正確，跳轉到首頁
        return redirect('/index')
    else:
        # 用戶明和密碼錯誤，跳轉到登錄頁面
        return redirect('/login')


# /test_ajax
def ajax_test(request):
    '''顯示ajax頁面'''
    return render(request, 'booktest/test_ajax.html')


def ajax_handle(request):
    '''ajax請求處理'''
    # 返回的json數據{'res':1}
    return JsonResponse({'res':1})

# /login_ajax
def login_ajax(request):
    '''顯示ajax登錄頁面'''
    return render(request, 'booktest/login_ajax.html')

# /login_ajax_check
def login_ajax_check(request):
    '''ajax登錄校驗'''
    # 1.獲取用戶名和密碼
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 2.進行校驗，返回json數據
    if username == 'ankle' and password == '123':
        # 用戶名密碼正確
        return JsonResponse({'res':1})
        # return redirect('/index') ajax請求在後台，不要返回頁面或者重定向
    else:
        # 用戶名或密碼錯誤
        return JsonResponse({'res':0})