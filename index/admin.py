from django.contrib import admin

# Register your models here.
from index.models import Book, Author,UserInfo,PubName,ExtendUserinfo #这个需要我们自己导入相应的模型类（数据表）
admin.site.register([Author,UserInfo])
@admin.register(Book) #使用admin.register(Model)来注册
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','retail_price','pub_name']
    def pub_name(self,obj):  #显示约束字段pubname
        return u'%s'%obj.pub.pubname  #u会对字符串中的\n等进行转义
    pub_name.admin_order_field = 'pub'  # 字段排序
    pub_name.short_description = '出版社'  # 属性name重命名
    list_display_links = ['title']
    list_filter = ['pub__pubname',]#ForeignKey字段
    list_editable=['price','retail_price']
    search_fields = ['title','pub__pubname']
    raw_id_fields = ['pub']
