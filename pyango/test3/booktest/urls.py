from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index), # 首頁
    # url(r'^showarg(\d+)$', views.show_arg),  # 捕獲url參數，(\d+) : 位置參數
    url(r'^showarg(?P<num>\d+)$', views.show_arg),  # 捕獲url參數，(\d+) : 關鍵字參數
    url(r'^login$', views.login), # 顯示登錄頁面
    url(r'^login_check$', views.login_check), # 用戶登錄校驗

    url(r'^test_ajax$', views.ajax_test), # 顯示ajax頁面
    url(r'^ajax_handle$', views.ajax_handle), # ajax處理
    url(r'^login_ajax$', views.login_ajax), # 顯示ajax登錄頁面
    url(r'^login_ajax_check$', views.login_ajax_check), # 顯示ajax登錄校驗
]
