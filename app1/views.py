from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def page_view(request):
    html='<h1>欢迎来到，C语言中文网，网址是http://c.biancheng.net</h>'
    return HttpResponse(html)