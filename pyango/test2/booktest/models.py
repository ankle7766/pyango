from django.db import models

# Create your models here.

# 一類
class BookInfo(models.Model):
    '''圖書模型類'''
    # 圖書名稱
    btitle = models.CharField(max_length=20, db_column='title')
    # 書名唯一
    # btitle = models.CharField(max_length=20, unique=True)
    # 出版日期
    bpub_date = models.DateField()
    # 閱讀量
    bread = models.IntegerField(default=0)
    # 評論量
    bcomment = models.IntegerField(default=0)
    # 刪除標記
    isDelete = models.BooleanField(default=False)


# 多類
class HumanInfo(models.Model):
    '''人物模型類'''
    # 人物名
    hname = models.CharField(max_length=20)
    # 性別
    hgender = models.BooleanField(default=False)
    # 備註
    hcomment = models.CharField(max_length=200, null=True, blank=True)
    # 關係(聯)屬性
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    # 刪除標記
    isDelete = models.BooleanField(default=False)

class BooktestBookinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField()
    bcomment = models.IntegerField()
    isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booktest_bookinfo'


class BooktestHumaninfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    hname = models.CharField(max_length=20)
    hgender = models.IntegerField()
    hcomment = models.CharField(max_length=200)
    isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.
    hbook = models.ForeignKey(BooktestBookinfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'booktest_humaninfo'


#新聞類型類
class NewsType(models.Model):
    #類型名
    type_name = models.CharField(max_length=20)
    # 關係屬性，代表類型下面的信息。定義在哪都可以
    type_news= models.ManyToManyField('NewsInfo')


#新聞類
class NewsInfo(models.Model):
    # 新聞標題
    title = models.CharField(max_length=128)
    # 發布時間
    pub_date = models.DateTimeField(auto_now_add=True)
    # 信息內容
    content = models.TextField()
    # 關係屬性，代表信息所屬的類型
    news_type = models.ManyToManyField('NewsType')

# 員工基本信息類
class EmployeeBasicInfo(models.Model):
    # 姓名
    name = models.CharField(max_length=20)
    # 性別
    gender = models.BooleanField(default=True)
    # 年齡
    age = models.IntegerField()
    # 關係屬性,代表員工的詳細信息
    employee_detail = models.OneToOneField('EmployeeDetailInfo')


#員工詳細信息類
class EmployeeDetailInfo(models.Model):
    # 聯繫地址
    addr = models.CharField(max_length=256)
    # 教育經歷
    # 關係屬性，代表員工的基本信息
    # employee_basic = models.OneToOneField('EmployeeBasicInfo')






class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'