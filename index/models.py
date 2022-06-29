from django.db import models


from django.db import models
#新建出版社表
class PubName(models.Model):
    pubname=models.CharField('名称',max_length=255,unique=True)
#更改书籍信息表
class Book(models.Model):
    title=models.CharField(max_length=30,unique=True, verbose_name='书名')
    price=models.DecimalField(max_digits=7,decimal_places=2,verbose_name='定价')
    #添加默认价格
    def default_price(self):
        return '￥30'
    #零售价格
    retail_price=models.DecimalField(max_digits=7,decimal_places=2,verbose_name='零售价',default=default_price)
    pub=models.ForeignKey(to=PubName,on_delete=models.CASCADE ,null=True) #创建Foreign外键关联pub,以pub_id关联
    def __str__(self):
        return "title:%s pub:%s price:%s" % (self.title, self.pub, self.price)


class Author(models.Model):  # 创建作者表
    name = models.CharField(max_length=30, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    books = models.ManyToManyField(to="Book")
    def __str__(self):
        return '作者：%s' % (self.name)


class UserInfo(models.Model):  # 创建用户信息表
    username = models.CharField(max_length=24, verbose_name='用户注册')
    password = models.CharField(max_length=24, verbose_name='密码')
    # 定义chocies参数的对应关系，以元组（或者列表）的形式进行表述：
    choices = (
        ('M', '男性'),
        ('F', '女性'),
    )
    gender = models.CharField(max_length=2, choices=choices, default='M',verbose_name='性别')

class ExtendUserinfo(models.Model):
    user=models.OneToOneField(to=UserInfo,on_delete=models.CASCADE)
    signature=models.CharField(max_length=255,verbose_name='用户签名',help_text='自建签名')
    nickname=models.CharField(max_length=255,verbose_name='昵称',help_text='自建昵称')