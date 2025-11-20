---
title: 使用 Django 搭建一个登录页面
date: 2024-01-29
description: Django 是基于 Python 的网站后端语言
authors:
  - name: 寅默
    link: https://github.com/YinMo19
    image: https://github.com/YinMo19.png
excludeSearch: false
math: true
---

Django 是基于 Python 的网站后端语言，单独列出来一个章节似乎并不是很合适，但是如果从其逻辑和之前的 C 或 Pure Python 并不太一样的角度出发，似乎又可以理解。以我的角度看，Django 是一个动态的语言，它会运行到某个地方停住，然后等待一个用户发来一个 request，然后根据 request 做出反应。因而基于逻辑的不同，独立章节似乎便有必要了。(本来笔者是打算合并在第二章的，但是学习过后发现单列出来更为合适。)

### 搭建平台的准备工作

和之前的 C 或 Pure Python 不一样的是，django 会自动提前生成很多的文件。(这一部分我们只演示一次，之后的范例会直接讲述对`views.py`与`templates/<project_name>/<name>.html`的操作) 首先我们在 Linux/Mac 平台下的命令行输入

```
django-admin startproject mytest
```

就会在该目录下生成以下内容

```
/mytest
├── manage.py
└── mytest2
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

其中文件`manage.py`算是执行文件，我们很多操作，例如调出 Shell 或者是启动 Django 都是通过这个文件进行。我们会用到`setting.py`、`urls.py`来进行编写，而剩下的那些，暂时不会用到，也不要去动他们。

### 创建一个 APP

这里的 APP 并不是传统意义上的手机 APP，而是一个 Application，一个应用。一个 Django 项目中可能会含有许多的应用，这些应用分别处理不同的功能。

我们首先来创建一个应用，我们应该在`mytest`同级目录下，即在`mytest`目录下的命令行输入

```
python manage.py startapp login_app
```

来创建一个 app。(这里便是通过`manage.py)来创建一个app。`至此我们的文件结构应该是

```
/mytest
├── login_app
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── mytest2
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   └── settings.cpython-311.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

另外我们需要创建一个在 app 里面创建一个网站的模板，即 app 目录下创建一个文件夹`templates`，而后在这个目录下（可选择再嵌套一层与 app 同名的文件夹）写 app 的 html 文件。下面的 tree 并不是刚生成就是这样，这是已经运行过后的。

```
/mytest
├── db.sqlite3
├── login_app
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── models.cpython-311.pyc
│   │   └── views.cpython-311.pyc
│   ├── templates
│   │   └── login_app
│   │       └── login.html
│   ├── tests.py
│   └── views.py
├── manage.py
└── mytest
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   ├── settings.cpython-311.pyc
    │   ├── urls.cpython-311.pyc
    │   └── wsgi.cpython-311.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

其中`__pycache__`是执行之后的文件，我们无需重写。而我们现在需要在“主函数”(也就是主目录下的) 的`settings.py`中为 app 注册。即

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login_app.apps.LoginAppConfig',#这里是新增的行
]
```

其中新增的行表示文件`login_app/apps.py/`中的`class LoginAppConfig`。我们可以看一下这个文件内的内容。

```python
from django.apps import AppConfig


class LoginAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login_app'
```

这里面有 app 的名字。至此我们已经可以开一个新的命令行打开这个网站了——我们修改任何代码都会重新加载网站，不需要担心需要手动重启网站。启动网站在命令行输入如下。

```
python manage.py runserver
```

此后直接打开给出的网址即可。我们可以在输入的时候后面加上指定的端口，如果没有指定默认是 8000。

### 开始编写网站

我们编写的地方主要在`urls.py  views.py`以及你自创的 html 文件。其中的流程大概如此——我们先在`urls.py`中创建一个功能上类似于网站名的 urls，并调用`views.py`中的函数。`urls.py`严格来说是定义了“路由”，而`views.py` 里的各个函数是负责生成“响应”，也就是“网页”的部分，网站的内容本身我们可以在模板中创作。例如我们的`urls.py`中应该是

```python
from django.contrib import admin
from django.urls import path
from login_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login_func)
]
```

第七行是我们新增的内容，表示我们新创的一个路径。第三行说明第七行中我们对`login/` 的反应是调用`views.py`中的`login_func`函数来处理。

```python
#views.py
from django.shortcuts import render,redirect,HttpResponse
# Create your views here.


def login_func(request):
    if request.method == "GET":
        return render(request,"login_app/login.html")

    user_name = request.POST.get("user")
    user_password = request.POST.get("pwd")
    if user_name == "root" and user_password == "111":
        return redirect("https://arcaea.lowiro.com/")

    return render(request,"login_app/login.html",{"error":"用户名或密码错误"})
```

而`views.py`里面最重要的则是函数的输入是一个`request`。这个`request`是指一个包含用户所有请求的对象，它可以查看 `request.method` 的值获得请求的方法。这里对 GET 和 POST 种类的请求做了不同处理，这两种请求分别是进入网站的默认方式和提交表单的默认方式。

我们的`views.py`中对请求的方法进行判断，若是直接请求，也就是刚进入这个网站，那么就直接调用模板中的网站。模板如下

```html
<h1>Welcome</h1>

<form method="post" action="/login/">
  {% csrf_token %}
  <input type="text" name="user" placeholder="用户名" />
  <input type="password" name="pwd" placeholder="密码" />
  <input type="submit" value="提交" />
  <span style="color:red;"> {{error}}</span>
</form>
```

如果我们已经输入了用户名和密码，也就是提交了表单，这时候就是 (POST) 请求，那么我们读入用户名和密码，并利用`if`来进行判断。如果可以的话，那么就重定向到一个新的网页 (这里夹带了一点点私货，这是笔者最喜欢的游戏的官网。),否则我们就重新返回这个网页。

这里我们利用了错误输入。django 的 html 文件语法上是 django 定义的，也就是在生成真正的 html 文件前，会先对其编译，然后进行替换。如果我们没有指定信息，那么替换后的结果为空。利用这个特性，我们在输入错误之后对模板中的错误信息进行填充，这样我们就可以看到错误信息所在。需要注意的是我们在 html 模板中设置输入的时候添加了

```python
{% csrf_token %}
```

这是因为 django 会自动判断我们的输入是否真正的来源于这个网站，其方法就是利用上述的代码生成一段用于验证的码。这是 django 的一项自动的安全措施。
