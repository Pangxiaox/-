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

#### （引用自https://blog.csdn.net/ZCF1002797280/article/details/49559863 ）

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

