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

1. 在【Pycharm】的models.py中建表

2. 在【MySQL  Workbench】中建立一个数据库，然后在【Pycharm】中settings.py中的DATABASES部分修改为上面说的MySQL形式的，name为刚刚建立的数据库名，对应settings.py中INSTALLED_APPS里也要加入自己建立的app名字（python manage.py startapp myapp)

▲记得首先  `pip install mysqlclient` 安装驱动

3. 在【Pycharm】里进行数据库迁移（python manage.py makemigrations -> python manage.py migrate)

4. 既可以在【Pycharm】中操作数据库，也可以在【MySQL Workbench】中通过SQL语句操作数据库，然后在【Pycharm】视图层返回数据

##### （2）Django Admin管理

Django 自动管理工具是 django.contrib 的一部分，可以在项目的 settings.py 中的 INSTALLED_APPS 看到。

1. 激活管理工具

urls.py  (Pycharm专业版建立Django项目之后自动生成)

```python
# urls.py
from django.conf.urls import url
from django.contrib import admin
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
```

2. 使用管理工具

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



### 9.8 新的安排

今天开会了，这周主要安排就是数据库设计，今天先用excel做了我负责部分的属性名以及对应数据类型的设计，还没对数据库进行讨论优化，然后优化完毕之后应该就是打算在Pycharm的相应子应用下的models.py中建表了，然后进行数据库迁移，并尝试用加了模板的HTML代码实现POST和GET等相关请求。

⭐关于本项目的部分约定——

项目命名：CataractProject

子应用命名：InformTable

HTML：DetailInform.html



### 9.9 静态文件配置

项目中的CSS、图片、js都是静态文件。一般会将静态文件放到一个单独的目录中，以方便管理。由于有些静态文件在项目中是通用的，所以推荐放在项目的根目录下。

为了提供静态文件，需要配置两个参数：

- STATICFILES_DIRS 存放查找静态文件的目录
- STATIC_URL 访问静态文件的URL前缀

使用步骤：

1. 确保INSTALLED_APPS包含了 `django.contrib.staticfiles`

2. 在项目根目录下创建static_files目录来保存静态文件。

3. 在settings.py中修改静态文件的两个参数为：

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_files'),
]
```

4. 此时在static_files添加的任何静态文件都可以使用网址 /static/文件在static_files中的路径来访问了



### 9.10 Django路由（入门篇）

参考自 https://blog.csdn.net/lczdada/article/details/82818129 

##### 路由定义位置

Django的主要路由信息定义在工程同名目录下的urls.py文件中，该文件是Django解析路由的入口。

##### 路由解析顺序

Django在接收到一个请求时，从主路由文件中的urlpatterns列表中以由上至下的顺序查找对应路由规则，如果发现规则为include包含，则再进入被包含的urls中的urlpatterns列表由上至下进行查询。

```python
urlpatterns = [
    url(r'^say', views.say),
    url(r'^sayhello', views.sayhello),
]
```

▲如上图，即使访问sayhello/路径，预期应该进入sayhello视图执行，但实际优先查找到了say路由规则也与sayhello/路径匹配，实际进入了say视图执行。

⭐好像是当url结尾没有斜线 / 的时候会发生上述错误，而当url结尾加上了斜线 / 时错误不会发生。如url(r'^say/',views.say)和url(r'^sayhello/', views.sayhello)

##### 路由命名与reverse反解析

1. 路由命名

（1）在使用include函数定义路由时，可以使用namespace参数定义路由的命名空间。

```python
url(r'^users/', include('users.urls', namespace='users')),
```

命名空间表示，凡是users.urls中定义的路由，均属于namespace指明的users名下。

命名空间的作用：避免不同应用中的路由使用了相同的名字发生冲突，使用命名空间区别开

（2）定义普通路由，可以使用name参数指明路由的名字。

```python
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^say', views.say, name='say'),
]
```

2. reverse反解析

```python
from django.core.urlresolvers import reverse


def index(request):
    return HttpResponse("hello the world!")


def say(request):
    url = reverse('users:index')  # 返回 /users/index/
    print(url)
    return HttpResponse('say')
```

- 对于未指明namespace的，reverse(路由name)
- 对于指明namespace的，reverse(命名空间namespace:路由name)

##### 路径结尾斜线 / 的说明

Django中定义路由时，通常以斜线/结尾，其好处是用户访问不以斜线/结尾的相同路径时，Django会把用户重定向到以斜线/结尾的路径上，而不会返回404不存在。

```python
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]
```

用户访问 index 或者 index/ 网址，均能访问到index视图。

##### 关于url的其他说明

- 每个正则表达式前面的'r' 是可选的但是建议加上。
- ^是起始符号，$是终结符号。如url(r'^index/$' , views.index)

⭐感觉URL路由这块还是有很多东西值得推敲的，明天继续研究



### 9.11 初步完成本周工作

今天没继续学Django相关知识，初步完成了本周的工作，设计了病历的Part 1 & Part 2 的数据库设计（models.py建表，迁移，与MySQL进行连接）。数据库原来设计的boolean和json数据类型是通过使用Django里的choices实现的，设置是否选项等，然后存数据库的是varchar类型，暂时不清楚这种操作是否会对数据库性能产生影响。另外，优化了病历页面时间日期（date、datetime-local）的显示，即默认显示用户登陆时的时间。



### 9.15 病历部分优化

还是在学校里工作效率高~~

之前的页面遇到一个问题就是都是数据库新增的，导致每次填写时都会新建对象，而且难以实现随时多次重复填写修改的情况，现在通过参考网上资料例子，对代码作出了较大的改动，现在可以多次对病历信息进行修改，与数据库实现同步。主要代码放到了GitHub上。

⭐关键代码如下：

```python
def editdiagnose(request, id):
    personal_info = PersonalInformation.objects.get(id=id) # 返回一个对象
    if request.method == "GET":
        return render(request, "CheckInform.html", {"personal_info":personal_info})
    else:
        # part 1
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        nation = request.POST.get("nation")
        #omit something
       
        p_info = PersonalInformation.objects.filter(id=id)  # 返回的是一个对象列表,QuerySet
        
        p_info.update(age=age)
        p_info.update(name=name)
        p_info.update(sex=sex)
        p_info.update(nation=nation)
        #omit something
```

```html
 <li><a href="{% url 'edit' items.id %}">编辑</a></li>
```

```python
urlpatterns = [
  	#omit something
    url(r'^editdiagnose/(?P<id>[0-9]*)/edit$', views.editdiagnose, name="edit"),
]
```

1. 关于editdiagnose方法：

A. 多参数问题——要在editdiagnose方法中添加一个参数id，其次还要在url中把这个id传递进去。

B. 如果是单纯查看功能，即if部分代码，GET，然后在对应的HTML的部分标签里添加如下所示的value属性之类，以select、input、textarea三个为例：

```html
<div class="col-sm-2">
	<label>性别：</label>
		<select class="form-control" name="sex">
			<option value="男" {% if personal_info.sex == "男" %} selected="selected" {% endif %}>男</option>
			<option value="女" {% if personal_info.sex == "女" %} selected="selected" {% endif %}>女</option>
		</select>
</div>
```

⚪select下拉选择框，加以{% if %}判断数据库内容来确定默认显示的值

```html
<div class="col-sm-2">
	<label>姓名：</label>
		<input type="text" name="name" class="form-control" value="{{ personal_info.name }}">
</div>
```

⚪input普通输入框，加入value属性

```html
<div class="col-sm-5 col-sm-offset-1">
    <div class="form-group">
        <label>主诉</label>
           <textarea name="main_suit" class="form-control" placeholder="" rows="6">{{ essential_info.main_suit }}</textarea>
     </div>
</div>
```

⚪textarea文本框，因为没有value属性，所以可以直接作为文本框内容

C. 如果需要做出修改功能，即else部分代码，重新获取一次输入框的值，然后再做更新操作。

2. 关于urlpatterns：将正则的内容括起来进行书写。优化正则匹配，注意P是大写不是小写，且这个组名必须和加到参数名保持一致（本例子里是id）

   ▲一个url例子： http://127.0.0.1:8000/editdiagnose/999999/edit （999999为id）

3. 关于上面的HTML一行代码：template中可以使用**"{% url  'app_name:url_name'  param %}"**来完成对应的url的跳转。其中app_name是应用名，url_name是目标网址，param是地址的参数。

   ▲由于我们只有一个根目录下的urls.py，所以可以按上图所示，只需要url_name，即对应urlpatterns里的url的name。



### 9.16 医生登录页面初步完成 + 病历页面再度优化 + 未决问题

1. 用了yy给的模板完成了医生登录页面，目前只是静态界面，后期再来讨论细化动态内容和优化调整页面样式。
2. 病历页面调整了title部分的几项信息，把后面的“是与否”选项的value属性改为“有与无”，为了和建表时的choices对应起来，优化了一些html文件的命名。

🍉（So far 我想到的，后面想到再加）部分待讨论和解决的问题：

1. 眼部检查部分的HTML代码在yy那里改了部分样式，未并入我这边。
2. 病历部分HTML代码在yy那里有改动，未并入我这边。如诊断结果部分加上了病情严重程度等输入框。
3. 在病历当中，婚姻和出生地在两个部分（两个表）中都出现了，另外title部分几项和下面部分的姓名、年龄、性别信息也重复出现了，目前用户是需要填写两次信息，是否需要确保这些值两次都是相同？如何确保？可否只填一次然后第二次时自动为用户显示第一次填写时的值？
4. 在病历中，出现了月经史，但只针对女性，那么男性是否需要处理相关信息？是否可根据一开始填写时的性别来判断页面应该显示月经史（女性）还是xx史（男性，注：xx表示暂不确定要用什么词语）？
5. 准备来合并yy和zz的代码，到时注意合并前后部分数据库信息和部分变量命名的一致性。
6. 登录页面的字段表单验证，目前已通过django实现部分验证，后续再看怎么解决（js / 原来模板已经提供（我忘了要看看）？）



### 9.17 添加删除病历功能

与编辑修改病历部分相似，增加了删除病历的功能。

🍌明天开会讨论记得要解决上述几个问题&已完成部分的合并



### 9.21 增加医生注册和登录界面1.0版本

开会改到了今天晚上~~那就先小结一下这阶段我所做的东西叭🍉

利用Django自带的登陆认证功能，完成了医生端登录和注册的部分功能，字段及表单验证尚未解决，目前来看还是通过js去操作表单验证方面的功能会更方便（在django里尝试了很多遍感觉有点难度，不过好像yy给的模板是有提供的，这个待看~~）

关键代码如下：

InformTable/models.py

```python
from django.contrib.auth.models import AbstractUser

class DoctorLogin(AbstractUser):
    docname = models.CharField(max_length=10)
    hosid = models.CharField(max_length=20)
    hosname = models.CharField(max_length=20)
```

扩展自带的User，在username、password的自带属性基础上加上了docname（医生姓名）、hosid（医院编号）、hosname（医院名字）这几个属性。

InformTable/views.py

```python
def doctorsignup(request):
    state = ""
    if request.method == 'POST':
        username = request.POST.get('docid', '') # 相当于django自带user验证的username
        hosid = request.POST.get('hosid', '')
        hosname = request.POST.get('hosname', '')
        password = request.POST.get('docpwd', '') #相当于django自带user验证的password
        docname = request.POST.get('docname', '')
        repeat_password = request.POST.get('repeat_docpwd', '')

        if DoctorLogin.objects.filter(username=username):
            state = '用户已存在'
        else:
            new_user = DoctorLogin.objects.create_user(username=username, password=password, hosid=hosid, hosname=hosname, docname=docname)
            new_user.save()

            return redirect('/doctorlogin/')

    return render(request, 'DoctorSignUp.html', {'state': state, 'user': None})


def doctorlogin(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get('docid')
        password = request.POST.get('docpwd')
        user = authenticate(username=username, password=password) # 其他字段对这个没影响
        if user is not None:
            login(request, user)
            return redirect('/patientslist/')
        else:
            message = "用户名或密码错误,请重新输入"
    return render(request, "DoctorLogin.html", {"message": message})


@login_required
def doctorlogout(request):
    logout(request)
    return redirect('/doctorlogin/')
```

注册、登录、注销三大主要功能的实现

settings.py

```python
LOGIN_URL = '/doctorlogin/' # 加了@login_required 未登录状态下自动跳转到登录页面
```

@login_required:需要在登录状态下操作的方法，添加上面这个LOGIN_URL之后，在未登录时试图访问对应方法的html页面时会自动重定向到登陆页面



### 9.22 原来bug是会越来越多的

今天合并完部分代码，然后，就有很多bug出现了（大哭）。



### 9.23 fix some bugs -> 开心起来了

解决的bug主要有：

1. 眼部检查部分数据库FloatField原来在不输入任何值的时候提交表单会出错，然后自己加了blank=True、null=True之后感觉没有起到效果，最后在HTML代码里设置默认值为0，确保在没有填写（尚未填写到）对应数值时还是可以成功保存一遍病历信息的。
2. 之前的页面跳转功能出现了可以跳到上一页，但不能跳到下一页（好奇怪啊这个bug），然后是因为form表单必须在整个div块区域里面，最后也解决了，同时引申出来的提交按钮放置位置问题也解决了，现在是在每一个小分页正下方底部都会有一个绿色提交按钮。
3. 对于月经史，如果一开始填写信息时（村委登记个人信息）填写的是“男”，那么第二页的月经史和相关备注不会显示出来，如果是“女”的话自然会显示出来。



