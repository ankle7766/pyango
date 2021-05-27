from django.db import models
# 設計和表對應的類，模型類
# Create your models here.

# 一類
#圖書類
class BookInfo(models.Model):
    '''圖書模型類'''
    #id不用定義，django會自己定義。
    # 圖書名稱，CharField說明是一個字符串，max_length指定字符串的最大長度
    btitle = models.CharField(max_length=20)
    # 出版日期，說明是一個日期類型
    bpub_date = models.DateField()

    def __str__(self):
        # 返回書名
        return self.btitle

# 多類
# 人物類
# 名字 hname
# 性別 hgender
# 年齡 hage
# 備註 hcomment
# 關係屬性 hbook，建立圖書類和英雄人物類之間的一對多關係
class HumanInfo(models.Model):
    '''人物模型類'''
    hname = models.CharField(max_length=20)     #人物名稱
    # 性別，布林值類型，default指定默認值，false代表男性
    hgender = models.BooleanField(default=False)
    # 備註
    hcomment = models.CharField(max_length=128)
    # 關係屬性 hbook，建立圖書類和英雄人物類之間的一對多關係
    # 關係屬性對應的表的字段名格式；關係屬性名_id。外鍵--foreign_key連到主鍵，建立外鍵關係。
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)

    def __str__(self):
        # 返回人名
        return self.hname



