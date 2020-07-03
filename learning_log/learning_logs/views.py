from django.shortcuts import render,redirect
from . import models

# Create your views here.
def index(request):
    """学习笔记的主页"""
    return  render(request, 'templates/index.html')


def register(request):
    #定义了个错误提示为空
    error_name = ''
    user = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    user_list = models.User.objects.filter(username=user)
    if request.method == 'POST':
        if user_list:
            # 注册失败
            error_name = '%s用户名已经存在了' % user
            # 返回到注册页面，并把错误信息报出来
            return render(request, 'login.html', {'error_name': error_name})
        else:
            # 数据保存在数据库中，并返回到登录页面
            user = models.User.objects.create(username=user, password=password, email=email)
            # 不知道这个save的作用
            user.save()
            return redirect('/register/')
    return render(request, 'login.html')

def login(request):
    print('获取的数据', request)
    # 定一个为空的数据接收
    error_msg = ''
    if request.methd == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 判断数据库中有没有账号密码
        ret = models.User.objects.filter(username=username, password=password)
        if ret:
            # 查询到用户信息
            return redirect('/index/')
        else:
            # 登录失败
            error_msg = '用户名或密码错误，请重新输入！'
    return  render(request, 'login.html', {'error_msg': error_msg})
