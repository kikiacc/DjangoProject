
from django.urls import path
from index import views
app_name='index'
urlpatterns=[
#127.0.0.1:8000/index/test 访问子模板
#path('test/',views.index_html),
#127.0.0.1:8000/index/base 访问父模板
path('base/',views.base_html),
path('test/',views.index_html,name='detail_hello'),
path('reverse/',views.test_to_reverse),
path('allbook/',views.BookName),
# path('login/',views.login),
path('set_cookie/',views.set_cookie_view),
path('get_cookie/',views.get_cookie_view),
# path('reg/',views.reg_view),

path('search_title_form/',views.search_ttile_form),
path('search_title/',views.search_title),
path('all_book/',views.book_table),
path('add_book/',views.add_book),
path('book_not_list/',views.book_not_list),
path('update_book/<int:book_id>/',views.update_book),
path('delete_book/<int:book_id>/',views.delete_book),
path('user_add_form/',views.user_add_form),
    path('page_test/',views.page_test),
path('send_mail/',views.send_email),
]