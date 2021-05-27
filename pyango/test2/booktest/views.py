from django.shortcuts import render, redirect   #導入重定向函數
from booktest.models import BookInfo, AreaInfo
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def index(request):
    '''顯示圖書信息'''
    # 1.查詢出所有圖書的信息
    books = BookInfo.objects.all()
    # 2.使用模板
    return render(request, 'booktest/index.html', {'books':books})

def create(request):
    '''新增一個圖書'''
    # 1.創建BookInfo對象
    b = BookInfo()
    b.btitle = '流星蝴蝶劍'
    b.bpub_date = date(1990,1,1)
    # 2.保存進數據庫
    b.save()
    # 3.返回應答，讓瀏覽器再訪問/index，重定向
    # return HttpResponse('OK')
    # return HttpResponseRedirect('/index')
    return redirect('/index')

def delete(request, bid):
    '''刪除典籍的圖書'''
    # 1.通過bid獲取圖書對象
    book = BookInfo.objects.get(id=bid)
    # 2.刪除
    book.delete()
    # 3.重定向，讓瀏覽器訪問/index
    # return HttpResponseRedirect('/index')
    return redirect('/index')

def areas(request):
    '''獲取廣州市的上級地區和下級地區'''
    # 1.獲取廣州市的信息
    area = AreaInfo.objects.get(atitle='广州市')
    # 2.查詢廣州市的上級地區
    parent = area.aParent
    # 3.查詢廣州市的下級地區
    children = area.areainfo_set.all()
    # 使用模板
    return render(request, 'booktest/areas.html', {'area':area, 'parent':parent, 'children':children})











