
from django.urls import path
from user import views
app_name='user'
urlpatterns=[
path('reg/',views.reg_view),
    path('login/',views.login_view),
path('logout/', views.logout_view)
]