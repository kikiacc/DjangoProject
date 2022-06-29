from django import template
register = template.Library()

#注册自定义简单标签
@register.simple_tag
def addstr_tag(strs):
    return 'Hello'%strs

#注册自定义引用标签
@register.inclusion_tag('inclusion.html',takes_context=True)
#定义函数渲染模板文件 inclusion.html
def add_webname_tag(context,namestr): #使用takes_context=True此时第一个参数必须为context
    return {'hello':'%s %s'%(context['varible'],namestr)}

@register.filter
def hello_my_filter(value):
    return value.replace('django','Python')

@register.filter(name='prefix')#使用name参数指定别名
def sorted_filter(value):
    return sorted(value)