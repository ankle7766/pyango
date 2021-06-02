from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index), # 首頁
    # url(r'^showarg(\d+)$', views.show_arg),  # 捕獲url參數，(\d+) : 位置參數
    url(r'^showarg(?P<num>\d+)$', views.show_arg),  # 捕獲url參數，(\d+) : 關鍵字參數
    url(r'^login$', views.login), # 顯示登錄頁面
]
