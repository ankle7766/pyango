from django.conf.urls import url
from booktest import views
# /index
# /index2
# 在應用的urls文件中進行url配置的時候:
# 1.嚴格匹配開頭和結尾
urlpatterns = [
    # 通過url函數配置url路由配置項
    url(r'^index$', views.index),  # 建立/index和試圖index之間的關係
    url(r'^index2$', views.index2),
    url(r'^books$', views.show_books), # 顯示圖書信息
    url(r'^books/(\d+)$', views.detail), # 顯示人物信息
]