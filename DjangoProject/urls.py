"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
# from app1 import views
from index import views
from index import urls as index_urls
from user import urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('page/', views.page_view),
    path('test/',views.test_html),
    path('test_html/',views.test_html),
    path('test_if/',views.test_if),
    path('Hello_MyWeb/<int:id>',views.Hello_MyWeb,name='hello'),
    path('test_for/',views.test_for),
    path('test01_for/',views.test01_for),
    path('test_url/',views.test_url),
    path('index/',include(index_urls)),
    path('redict/',views.redict_url),
    path('user/',include(user_urls))
]

