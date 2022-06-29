import hashlib

from DjangoProject import settings
from index.forms import TitleSearch, UserModelForm  # 引入forms.py中定义的TitleSearch类
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core import mail

# Create your views here.
#方式一
from django.template import loader # 导入loader方法
from django.shortcuts import render #导入render 方法
# def test_html(request):
#     t=loader.get_template('test.html')
#     html=t.render({'name':'c语言中文网'})#以字典形式传递数据并生成html
#     return HttpResponse(html) #以 HttpResponse方式响应html
#方式二
# from django.shortcuts import render #导入reder方法
# def test_html(request):
#     return render(request,'test.html',{'name':'c语言中文网'})#根据字典数据生成动态模板
from django.urls import reverse

from index.models import Book, PubName, UserInfo


def test_html(request):
    a={} #创建空字典，模板必须以字典的形式进行传参
    a['name']='C语言中文网'
    a['course']=["Python","C","C++","Java"]
    a['b']={'name':'C语言中文网','address':'http://c.biancheng.net/'}
    a['test_hello']=test_hello
    a['class_obj']=Website()
    return render(request,'test_html.html',a)
def test_hello():
    return '欢迎来到C语言中文网'
class Website:
    def Web_name(self):
        return 'Hello，C语言中文网!'
    #Web_name.alters_data=True #不让Website()方法被模板调用

#在views.py 中添加如下代码
def test_if(request):
    dic={'x':2**4}
    return render(request,'test_if.html',dic)

from django.template import Template,Context#调用template、以及上下文处理器方法
def Hello_MyWeb(request,id):
      #调用template()方法生成模板
      t=Template("""
                        {% if web.name == 'C语言中文网' %}
                              {% if printable %}
                                     <h1>Hello C语言中文网</h1>
                              {% else %}
                                      <h2>欢迎您下次访问，C语言中文网</h2>
                              {% endif %}
                        {% endif %}
                                      """)
      c= Context({'web':{'name':'C语言中文网'}, 'printable' : True }) #Context必须是字典类型的对象，用来给模板传递数据
      html=t.render(c)
      return HttpResponse(html)

from django.template import Template,Context
def test_for(request):
      #调用template()方法生成模板
      t1=Template("""
                    {% for item in list %}
                        <li>{{ item }}</li>
                    {% empty %}
                        <h1>如果找不到你想要，可以来C语言中文网(网址：http://c.biancheng.net/)</h1>
                    {% endfor %}
                              """)
      #调用 Context()方法
      c1= Context({'list':['Python','Java','C','Javascript','C++']})
      html=t1.render(c1)
      return HttpResponse(html)

def test01_for(request):
    #使用嵌套for标签依次遍历列表取值
     website=Template("""
     {% for course in list01 %}
     <div>
        {% for coursename in course %}
        <p><b>{{ coursename }}</b></p>
        {% endfor %}
     </div>
     {% endfor %}
     """)
     webname=Context({'list01':[['Django','Flask','Tornado'],['c语言中网','Django官网','Pytho官网']]})
     html=website.render(webname)
     return HttpResponse(html)


def test_url(request):
    return render(request,'test_url.html')


#定义父模板视图函数
def base_html(request):
    return render(request,'index/base.html')
#定义子模板视图函数
def index_html(request):
    name='xiaoming'
    course=['python','django','flask']
    return render(request,'index/test.html',locals())


def redict_url(request):
    return render(request,'index/newtest.html')

#reverse函数实现反向解析重定向到我们想要的有页面
def test_to_reverse(request):
    return HttpResponseRedirect(reverse('index:detail_hello'))

def BookName(request):
    books=Book.objects.raw("select * from index_book") #书写sql语句
    return render(request,"index/allbook.html",locals())


#第一步index/views.py 创建Form对象。
from django import forms
class LoginForm(forms.Form): #继承自Form类，
    user_name=forms.CharField(label="用户名",min_length=6,max_length=12)#新建表单字段
    user_password=forms.CharField(label="用户密码",min_length=8)

#第二步围绕form对象完成表单。
def login(request):#定义登录处理函数login()
    if request.method == "POST": #request是 HttpRequest的对象，利用它的的method属性，判断请求方法。
        form = LoginForm(request.POST)#实例化对象，post提交数据是QuerySet类型的字典，GET方法与其一样。
        if form.is_valid(): #提供验证判断是否有效，成立则返回是Ture
            return HttpResponse("登录成功")
    else:
        form=LoginForm()
    return render(request, "index/login.html",locals())



#设置添加cookie
def set_cookie_view(request):
    resp=HttpResponse()
    resp.set_cookie('username','cbiancheng',3600)
    return resp
#得到cookie的值使用get方法
def get_cookie_view(request):
    value = request.COOKIES.get('username')
    return HttpResponse('--MY COOKIE is--%s'%value)


#用户的登录逻辑处理
def login_view(request):
    #处理GET请求
    if request.method == 'GET':
        #1, 首先检查session，判断用户是否第一次登录，如果不是，则直接重定向到首页
        if 'username' in request.session:  #request.session 类字典对象
            return HttpResponseRedirect('/index/allbook')
        #2, 然后检查cookie，是否保存了用户登录信息
        if 'username' in request.COOKIES:
            #若存在则赋值回session，并重定向到首页
            request.session['username'] = request.COOKIES['username']
            return HttpResponseRedirect('/index/allbook')
        #不存在则重定向登录页，让用户登录
        return render(request, 'user/login.html')
    # 处理POST请求
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        m = hashlib.md5()
        m.update(password.encode())
        password_m = m.hexdigest()
        #判断输入是否其中一项为空或者格式不正确
        if not username or not password:
            error = '你输入的用户名或者密码错误 !'
            return render(request, 'user/login.html', locals())
        #若输入没有问题则进入数据比对阶段，看看已经注册的用户中是否存在该用户
        users = User.objects.filter(username=username, password=password_m)
        # 由于使用了filter, 所以返回值user是一个数组，但是也要考虑其为空的状态，即没有查到该用户
        if not users:
            error = '用户不存在或用户密码输入错误!!'
            return render(request, 'user/login.html', locals())
        # 返回值是个数组，并且用户名具备唯一索引，当前用户是该数组中第一个元素
        users = users[0]
        request.session['username'] = username
        response = HttpResponseRedirect('/index/allbook')
        #检查post 提交的所有键中是否存在 isSaved 键
        if 'isSaved' in request.POST.keys():
            #若存在则说明用户选择了记住用户名功能，执行以下语句设置cookie的过期时间
            response.set_cookie('username', username, 60*60*24*7)
        return response

#用来显示查询页面
# def search_ttile_form(request):
#     return render(request,'index/search_title.html')
#用来显示查询结果
# def serch_title(request):
#     if not request.GET.get('title', ''):
#         errors = ['输入的书名是无效']
#         # 在这里使用列表的原因，是因为随着表单功能的修改可能需要传递多个字段，这时可能会有多个不同的错误信息需要展示。
#         return render(request, 'index/search_title.html', locals())
#     title = Book.objects.filter(title__icontains=request.GET['title'])
#     # print(request.GET['title'])
#     # print(title.count())
#     if title.count()==0:
#         return render(request, 'index/search_title.html', {'errors':['无结果']})
#     return render(request, 'index/book_list.html', locals())

def book_table(request):
    try:
        all_book=Book.objects.all().order_by('-price')
        if not all_book:
            return HttpResponse('书籍信息表为空，请录入！')
    except Exception as e:
        print(e)
    return render(request, 'index/book_table.html', locals())


def add_book(request):
    if request.method == 'GET':
        return render(request, 'index/add_book.html')
    elif request.method == 'POST':
        #添加书籍
        title = request.POST.get('title')
        if not title:
            return HttpResponse('请给出一个正确的title')
        pub = request.POST.get('pub')
        price = float(request.POST.get('price','999.99'))
        if not price:
            return HttpResponse('请输入价格')
        try:
            retail_price = float(request.POST.get('retail_price'))
            if not retail_price:
                return HttpResponse('请输入市场价')
        except Exception as e:
            print(e)

        #判断title是不是已经存在了
        old_book = Book.objects.filter(title=title)
        if old_book:
            return HttpResponse('你输入的书籍系统已经存在 !')
        try:
            pub1=PubName.objects.get(pubname=str(pub))
            Book.objects.create(title=title,price=price,retail_price=retail_price,pub=pub1)
        except Exception as e:
            print('Add ErrorReason is %s'%(e))
        return HttpResponseRedirect('/index/all_book')
    return HttpResponse('请使用正确Http请求方法 !')


def search_ttile_form(request):
    return render(request,'index/search_title.html',context={'form':TitleSearch()})#实例化表单对象
def search_title(request):
    form=TitleSearch(request.GET)
    if form.is_valid():#第一步验证成功
        books=Book.objects.filter(title__icontains=form.cleaned_data["title"])#调用cleaned_data属性获取清理后的数据
        if not books:
            return HttpResponseRedirect("/index/book_not_list")
        return render(request,'index/book_list.html',locals())
    else:
        # 将带有错误信息的表单实例作为上下文传递到需要渲染的模板中
        return render(request,'index/search_title.html',{'form':form})
def book_not_list(request):
    return render(request,"index/book_not_list.html")

def update_book(request,book_id):
    #用 book_id给每个书籍加上标记
    #将其作为查找书籍的参数
    book_id = int(book_id)
    try:
        book = Book.objects.get(id=book_id)
    except Exception as e:
        return HttpResponse('--没有找到任何书籍---')
    if request.method=='GET':
        return render(request,'index/update_book.html',locals())
    elif request.method == 'POST':
        price = request.POST.get('price')
        retail_price=request.POST.get('retail_price')
        if not price or not retail_price:
            return HttpResponse('请输入更改后的零售价或市场价！')
        price=float(price)
        retail_price=float(retail_price)
        # 修改对象属性值
        book.price =price
        book.retail_price=retail_price
        # 存储更新后的状态
        book.save()
        #重定向至127.0.0.1:8000/index/all_book/
        return HttpResponseRedirect('/index/all_book')
    return HttpResponse("书籍信息更新功能")

def delete_book(request,book_id):
    book_id=int(book_id)
    try:
        book=Book.objects.get(id=book_id)
    except Exception as e:
        print('get查询出现了异常没找到数据',e)
        return HttpResponse('这里没有任何书籍可以被删除')
    if request.method=="GET":
        return render(request,'index/delete_book.html',locals())
    elif request.method=="POST":
        book.delete()
        return HttpResponseRedirect("/index/all_book")
    return HttpResponse("书籍条目信息删除功能")

def user_add_form(request):
    print("================")
    if request.method=="POST":
        print("----------------")
        user=UserModelForm(request.POST)
        if user.is_valid():
            user=UserInfo.objects.create(username=user.cleaned_data['username'],
                                         password=user.cleaned_data["password"],
                                         gender=user.cleaned_data['gender'])
            #user_add.html只需要接收变量{{ user }}即可
            return render(request,'index/user_add.html',locals())
        else:
            return render(request,'index/useradd_model_form.html',context={'form':user})
    else:
        return render(request,'index/useradd_model_form.html',{'form':UserModelForm()})

from django.core.paginator import Paginator#分页功能
#视图函数 index/views.py
def page_test(request):
    # 测试分页功能
    books=Book.objects.all()
    paginator = Paginator(books,2)
    num_p = request.GET.get('page',1)#以page为键得到默认的页面1
    page=paginator.page(int(num_p))
    return render(request,'index/page_test.html',locals())

def send_email(request):
    subject = '😴'  # 主题
    from_email = settings.EMAIL_FROM  # 发件人，在settings.py中已经配置
    to_email = ['zhangjing7@cib.com.cn','duanyaqi@cib.com.cn']  # 邮件接收者列表
    # 发送的消息
    message = '晚上好'  # 发送普通的消息使用的时候message
    # meg_html = '<a href="http://www.baidu.com">点击跳转</a>'  # 发送的是一个html消息 需要指定
    mail.send_mail(subject, message, from_email, to_email)
    return HttpResponse('OK,邮件已经发送成功!')