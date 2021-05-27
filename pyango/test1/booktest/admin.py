from django.contrib import admin
from booktest.models import BookInfo,HumanInfo
# 後臺管理相關文件
# Register your models here.
# 自定義模型管理類
class BookInfoAdmin(admin.ModelAdmin):
    '''圖書館模型類'''
    list_display = ['id','btitle','bpub_date']

class HumanInfoAdmin(admin.ModelAdmin):
    '''人物模型管理類'''
    list_display = ['id', 'hname', 'hcomment']
# 註冊模型類
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HumanInfo, HumanInfoAdmin)