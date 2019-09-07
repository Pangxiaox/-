### 8.30 Django初识

之前自己一直做的都是Java web,这次也是第一次接触python web，也同样是第一次用Django framework.

自己用的是pycharm IDE，因为之前用华工邮箱注册了个jetbrains账号，可以下载专业版，然后直接建立Django项目（亲测非常好用），然后通过在命令行中输入 `python manage.py startapp myapp`来创建一个名为myapp的文件夹，然后查阅了网上的资料写了个helloworld，很多东西还不算很懂，接下来打算再深入理解一下。



###  8.31 佛系CV（复制粘贴）的一天     

今天的我是个莫得感情的复制粘贴机器，写完了那个静态病历网页，有些地方我也不敢肯定是不是只需要某些信息，感觉还需要和欣然姐沟通一下，就是可能不同病人某些项目里需要获取到的信息也有一定不同，然后之前说用复选框的由于要选择的项目实在有点多最后我个人感觉还是用下拉选择框会比较简洁方便一点，然后Django框架等下再看明天再说框架的东西。



### 9.1 Django与数据库

#### 数据库操作基本流程

- 编辑 `models.py` 文件，改变模型。
- 运行 [`python manage.py makemigrations`](https://docs.djangoproject.com/zh-hans/2.1/ref/django-admin/#django-admin-makemigrations)   为模型的改变生成迁移文件。
- 运行  [`python manage.py migrate`](https://docs.djangoproject.com/zh-hans/2.1/ref/django-admin/#django-admin-migrate)  来应用数据库迁移。



1.数据库配置（默认SQLite）-> 2.创建模型（编写应用的models.py)  -> 3.安装应用（在settings.py中INSTALLED_APPS中添加需要安装的应用的apps.py文件中Config类，如 `helloapp.apps.HelloappConfig`) ->  4.生成迁移文件（见上） ->  5.执行数据库迁移（见上）

▲每次改变模型后都要做生成迁移文件和执行数据库迁移的操作。



#### 命令行中操作数据库

1.打开命令行（通过 `python manage.py shell`  命令打开 Python 交互式命令行） -> 2. `>>> from helloapp.models import Student  `（例子）-> 3.数据库CRUD（见下）



#### 数据库CRUD

#### （引用自https://blog.csdn.net/ZCF1002797280/article/details/49559863）

```python
  class Student():
        name = models.CharFiled(max_length = 30)
        age = models.IntegerFiled()
```

##### 增

```python
   stu1 = Student(name="Aaron", age=23)
   stu1.save() # flush到数据库中
```

或

```python
Student.objects.create(name="Aaron", age=23)
```

##### 删

删除表中所有数据:

```python
	Student.objects.all().delete()
```

删除name等于Aaron的数据:

```python
	Student.objects.get(name='Aaron').delete()
```

删除age等于20的<u>多条</u>数据

```python
	Student.objects.filter(age=20).delete()
```

##### 改

```python
   	stu = Student.objects.get(name='Aaron') # 查询该条记录
    stu.name = 'Zhang'                      # 修改
    stu.save()                              # 保存
```

更新多个字段

```python
	Student.objects.get(name='Aaron').update(name='Zhang', age=20)
```

更新所有字段

```python
	Student.objects.all().update(name='Zhang')
```

##### 查

查表中所有记录

```python
	Student.objects.all()
```

查询带字段名的所有记录，就是将所有记录以key-value的形式保存在字典中

```python
	Student.objects.all().values()
```

查询单条记录

```python
	Student.objects.get(name='Aaron')
```

▲查询name字段是Aaron的这条数据，如果返回多条记录或没有会报错，需结合`try/except`一起使用。

查询匹配条件的多条数据

```python
	Student.objects.filter(name='Aaron')
```

▲括号中匹配条件可多个，以逗号分隔。

模糊查询

```python
	Student.objects.filter(name__contains="A")
```



### 9.2 Django 模板系统

##### 常用操作

{{ }}表示变量，在模板渲染的时候替换成值，{% %}(表示标签)表示逻辑相关的操作

hello/views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

def template_test(request):

    class Person():
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def sleep(self):
            return "{}正在睡觉.".format(self.name)

    p1 = Person("Ann", 21)
    p2 = Person("Bob", 23)
    p_list = [p1, p2]
    lst = [11, 22, 33, "aa", "gg"]
    dst = {"hobby": "running", "age": 27}
    return render(request, "../templates/template_test.html", {"p_list": p_list, "lst": lst, "dst": dst})
```

hello/templates/template_test.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <p>
        取参数:{{ p_list.0.name }}
        <br/>
        取参数:{{ p_list.1.age }}
        <br/>
        取参数:{{ lst.2 }}
        <br/>
        取参数:{{ lst.4 }}
        <br/>
        取参数:{{ dst.hobby }}
        <br/>
        取参数:{{ p_list.0.sleep }}
    </p>

<ul>
    {% for person in p_list %}
        <li>{{ person.name }}</li>
        <li>{{ person.age }}</li>
    {% endfor %}
</ul>
<ul>
    {% for item in lst %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
{% if p_list %}
    人数:{{ p_list|length }}
    {% else %}
    没有人员
{% endif %}
</body>
</html>
```

urls.py

```python
from hello import views
urlpatterns = [
    url(r'^hello/', views.hello),
    url(r'^template_test/', views.template_test)
]
```

##### 过滤器

{{ value|filter_name:参数 }}

▲ ‘:’ 左右没有空格

- length

  {{ value|length }}返回value的长度

- upper/title/lower

  {{value|upper}}返回大写 {{value|lower}}返回小写 {{value|title}}让每个开头字母都大写

- first/last

  {{value|first}}取第一个元素 {{value|last}}取最后一个元素

- slice

  {{value|slice:"2:-1"}} python切片

##### 模板继承

主要是为了提高代码重用，减轻开发人员的工作量。

典型应用：网站的头部、尾部信息

⭕父模板：标签block用于在父模板中预留区域，留给子模板填充差异性的内容。建议给endblock标签写上名字，这个名字与对应的block名字相同。

⭕子模版：标签extends表示继承，写在子模版文件第一行。子模版不用填充父模版中的所有预留区域，如果子模版没有填充，则使用父模版定义的默认值。

templates/base.html（父模板）

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <h1>My helpful timestamp site</h1>
    {% block content %}{% endblock %}
    {% block footer %}
    <hr>
    <p>Thanks for visiting my site.</p>
    {% endblock %}
</body>
</html>
```

templates/current_datetime.html（子模板）

```html
{% extends "base.html" %}
{% block title %}The current time{% endblock %}
{% block content %}
<p>It is now {{ current_date }}.</p>
{% endblock %}
```

hello/views.py

```python
# omit something
def base(request):
    return render(request, "../templates/base.html", {"title" : "parent"})


def current_datetime(request):
    current_date=datetime.datetime.now()
    return render(request, "../templates/current_datetime.html", {"current_date": current_date})
```

urls.py

```python
from hello import views

urlpatterns = [
    # omit something
    url(r'^base/', views.base),
    url(r'^current_datetime/', views.current_datetime)
]
```

### 9.3 

今天有点忙，没干太多，然后在GitHub上找了一些例子准备看，先mark在这里：

https://github.com/snowWave1995/Student_management

https://github.com/jerrybox/StudentSystemAdmin

今天试了一下用MySQL作为数据库而不是默认的SQLite，需要先在命令行中使用 `pip install mysqlclient`来安装MySQL驱动。

settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test123',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```

通过这几天的学习，自己简单的写了一下比较基础的入门级的代码，不在命令行中操作数据库，而是直接定义一个函数来操作数据库，并使用了模板和视图，在网页上显示出数据库中的相关数据值。

### 9.4 Django表单

今天还是很忙，甚至比昨天还忙，哭唧唧，明天就有时间喇，可以去看之前说的GitHub项目例子了。今天帮小金同学解决了pycharm连接MySQL的问题，大家都要好好加油，做实干家！

代码参考自： https://www.runoob.com/django/django-form.html

##### HTTP请求之GET方法

hello/search.py

```python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response


# 表单
def search_form(request):
    return render_to_response('search_form.html')


# 接收请求数据，testinput对应HTML的输入框的name属性值
def search(request):
    request.encoding = 'utf-8'
    if 'testinput' in request.GET and request.GET['testinput']:
        message = '你搜索的内容为: ' + request.GET['testinput']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
```

templates/search_form.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <form action="/search" method="get">
        <input type="text" name="testinput">
        <input type="submit" value="搜索">
    </form>
</body>
</html>
```

##### HTTP请求之POST方法

▲表格后面还有一个{% csrf_token %}的标签。csrf 全称是 Cross Site Request Forgery。这是Django提供的防止伪装提交请求的功能。POST 方法提交的表格，必须有此标签。

hello/search2.py

```python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据，q对应HTML的输入框的name属性值
def search_post(request):
    ct = {}
    if request.POST:
        ct['rlttee'] = request.POST['q']
    return render(request, "post.html", ct)
```

templates/post.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <form action="/search_post" method="post">
        <!-- csrf_token必须 -->
        {% csrf_token %}
        <input type="text" name="q">
        <input type="submit" value="Submit">
    </form>

    <p>{{ rlttee }}</p>
</body>
</html>
```

### 9.5 新的尝试

今天，准确来说是昨天，自己写了一下，实现了填写表单POST之后页面跳转到指定页面显示出更新过的数据库内容的相关操作，代码直接上我的GitHub看叭。by the way -》GitHub断更了一天就好像签到断签一样难受（不是）

Student/models.py

```python
from django.db import models


class StudentInfo(models.Model):
    name = models.CharField(max_length=15)
    SEX_CHOICES =(
        ('男', 'male'),
        ('女', 'female'),
    )
    sex = models.CharField(max_length=2, choices=SEX_CHOICES)
    credit = models.IntegerField()
```

Student/views.py

```python
from Student.models import StudentInfo
from django.shortcuts import render, redirect


def show(request):
    studentlist = StudentInfo.objects.all()
    return render(request, "studentinfo.html", {"s_list": studentlist})


def post(request):
    stu = StudentInfo()
    ct = {}
    if request.POST:
        ct['name'] = request.POST['inputname']
        ct['sex'] = request.POST['inputsex']
        ct['credit'] = request.POST['inputcredit']
        stu.name = request.POST.get('inputname')
        stu.sex = request.POST.get('inputsex')
        stu.credit = request.POST.get('inputcredit')
        stu.save()
        return redirect("/studentinfo/")
    return render(request, "post.html", ct)
```

templates/post.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/postsomething" method="post">
    {% csrf_token %}
    <p>姓名</p>
    <input type="text" name="inputname">
    <p>性别</p>
    <select name="inputsex">
    <option value="男" name="男">男</option>
    <option value="女" name="女">女</option>
    </select>
    <p>学分</p>
    <input type="text" name="inputcredit">

    <input type="submit" value="Submit">
</form>

<p>{{ name }}</p>
&nbsp;&nbsp;
<p>{{ sex }}</p>
&nbsp;&nbsp;
<p>{{ credit }}</p>

</body>
</html>
```

templates/studentinfo.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<table>
    <tr>
        <td>名字</td>
        <td>性别</td>
        <td>学分</td>
    </tr>
    {% for listitems in s_list %}
        <tr>
          <td>{{ listitems.name }}</td>
          <td>{{ listitems.sex }}</td>
          <td>{{ listitems.credit }}</td>
        </tr>
    {% endfor %}
</table>

<hr/>
<p>学分合格的同学是：</p>
{% for listitems in s_list %}
        {%  if listitems.credit >= 125 %}
            {{ listitems.name }}
        {% endif %}
{% endfor %}
</body>
</html>
```

urls.py

```python
from django.contrib import admin
from django.conf.urls import url
from Student import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^studentinfo/', views.show),
    url(r'^postsomething$', views.post),
]
```

settings.py

```python
# 记得记得要加'Student'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Student'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'xxx',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

部分截图如下：

![Image text](https://github.com/Pangxiaox/Cataract-Platform/blob/master/Shot/1.PNG)
![Image text](https://github.com/Pangxiaox/Cataract-Platform/blob/master/Shot/2.PNG)

### 9.6 

今天在昨天代码基础上，融进了CSS和实现了点击“增加学生”填写完信息之后页面自动跳转回主界面，而且可以和数据库同步。具体代码见GitHub learningdjango文件夹。

新的截图如下：

![Image text](https://github.com/Pangxiaox/Cataract-Platform/blob/master/Shot/3.PNG)

##### （1）Django与MySQL Workbench

如果是使用MySQL作为数据库，最近总结了一份套路：

1.在【Pycharm】的models.py中建表

2.在【MySQL  Workbench】中建立一个数据库，然后在【Pycharm】中settings.py中的DATABASES部分修改为上面说的MySQL形式的，name为刚刚建立的数据库名，对应settings.py中INSTALLED_APPS里也要加入自己建立的app名字（python manage.py startapp myapp)

▲记得首先  `pip install mysqlclient` 安装驱动

3.在【Pycharm】里进行数据库迁移（python manage.py makemigrations -> python manage.py migrate)

4.既可以在【Pycharm】中操作数据库，也可以在【MySQL Workbench】中通过SQL语句操作数据库，然后在【Pycharm】视图层返回数据

##### （2）Django Admin管理

Django 自动管理工具是 django.contrib 的一部分，可以在项目的 settings.py 中的 INSTALLED_APPS 看到。

1.激活管理工具

urls.py  (Pycharm专业版建立Django项目之后自动生成)

```python
# urls.py
from django.conf.urls import url
from django.contrib import admin
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
```

2.使用管理工具

通过命令 **python manage.py createsuperuser** 来创建超级用户

```python
# python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@runoob.com
Password:
Password (again):
Superuser created successfully.
[root@solar HelloWorld]#
```

访问 http://127.0.0.1:8000/admin/ ，通过用户名密码登录

为了让 admin 界面管理某个数据模型，我们需要先注册该数据模型到 admin

myapp/admin.py

```python
from django.contrib import admin
from TestModel.models import Test
 
# Register your models here.
admin.site.register(Test)
```

### 9.7 又是一个ctrl-CV的一天

今天把之前做的病历页面成功地套用了一个模板，主要就是利用模板来调整版面样式。准备明天开会喇，这次不会鸽掉喇哈哈哈。

代码已经放在GitHub上了，主要是assets文件夹和diagnose_new.html

部分截图如下：

![Image text](https://github.com/Pangxiaox/Cataract-Platform/blob/master/Shot/4.PNG)

![Image text](https://github.com/Pangxiaox/Cataract-Platform/blob/master/Shot/5.PNG)

