from django.conf.urls import url

from App import views

urlpatterns = [
    # 首页
    url(r'^$',views.index_home,name='index_home'),
    # 登录
    url(r'^login/$',views.login,name='index_login'),
    # 注册
    url(r'^register/$',views.index_register,name='index_register')
]