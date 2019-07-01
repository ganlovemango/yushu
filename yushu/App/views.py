import hashlib
import re

from django.shortcuts import render

# Create your views
# 首页
from App.models import *


def index_home(request):
    return render(request,'index_home.html')
# 登录
def login(request):
    if request.method == 'POST':
        email = request.POST.get.email
        password = request.POST.get.password
        # 对密码进行hash1
        password = hashlib.sha1(password.encode('utf8')).hexdigest()









    return render(request,'index_login.html')
























# 注册
def index_register(request):
    if request.method == 'POST':
        a = 0
        b = 0
        c = 0
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        res = User.objects.all()
        print('aaaaaa',res)
        print('aaaaaaa',res)
        if not username:
            a = 1
        # elif username in res[0].username:
        elif User.objects.filter(username=username):
            a = 2
        elif not email:
            b = 1
        elif not re.match(r'^(\w{3,15})@(\w{2,5})\.(com|cn|net)$',str(email)):
            b = 2
        elif User.objects.filter(email=email):
            b = 3
        elif not re.match(r'[\w]{8,18}$',str(password)):
            c = 1
        elif str(password).isdigit():
            c = 2
        else:
            password = hashlib.sha1(password.encode('utf8')).hexdigest()
            user = User(username=username,password=password,email=email)
            user.save()
            request.session['username'] = username
            request.session['email'] = username
        if a > 0 or b > 0 or c > 0:
            return render(request,'index_register.html',context={
                'a':a,
                'b':b,
                'c':c
            })
        else:
            return render(request,'index_home.html',context={
                'username':username
            })
        #     return render(request, 'index_home.html')
    else:
        return render(request, 'index_register.html')