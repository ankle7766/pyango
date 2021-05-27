
from booktest import views
from django.conf.urls import url

urlpatterns = [
     url(r'^index$', views.index), # 圖書信息頁面
     url(r'^create$', views.create), # 新增一本圖書
     url(r'^delete(\d+)$', views.delete), # (\d)讓django框架進行地址匹配時，它能把這一部分的數字當作參數傳遞給視圖
     url(r'^areas$', views.areas),  #自關聯案例
]
