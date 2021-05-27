from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo
from django.template import loader,RequestContext

def my_render(request, template_path, context_dict={}):
    '''使用模板文件'''
    # 使用模板文件
    # 1.加載模板文件
    temp = loader.get_template(template_path)

    # 2.定義模板上下文:給模板文件傳遞數據
    # 舊版 : context = RequestContext(request, {})
    context = context_dict

    # 3.模板渲染:產生標準的html內容
    res_html = temp.render(context)

    # 4.返回給瀏覽器
    return HttpResponse(res_html)

# Create your views here.
# 1.定義視圖函數，httprequest
# 2.進行url配置，建立url地址和視圖的對應關係
# http://127.0.0.1:8000/index
def index(request):
    # 進行處哩，和M和T進行交互....
    # return HttpResponse('老鐵，沒毛病。')
    # return my_render(request, 'booktest/index.html')
    return render(request, 'booktest/index.html', {'content':'hello world', 'list':list(range(1,10))})


# http://127.0.0.1:8000/index2
def index2(request):
    # 進行處哩，和M和T進行交互....
    return HttpResponse('hello world!')

def show_books(request):
    '''顯示圖書的信息'''
    # 1.通過N查找圖書表中的數據
    books = BookInfo.objects.all()
    # 2.使用模板
    return render(request, 'booktest/show_books.html', {'books':books})

def detail(request, bid):
    '''查詢圖書關聯人物信息'''
    # 1.根據bid查詢圖書信息
    book = BookInfo.objects.get(id=bid)
    # 2.查詢和book關聯的人物信息
    humen = book.humaninfo_set.all()
    # 3.使用模板
    return render(request, 'booktest/detail.html', {'book':book, 'humen':humen})