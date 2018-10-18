[主页](https://github.com/greyli/helloflask)
/ [勘误](https://github.com/greyli/helloflask/blob/master/errata/errata.md)
/ FAQ
/ [可改进实现](https://github.com/greyli/helloflask/blob/master/improvement/improvement.md)
/ [版本更新记录](https://github.com/greyli/helloflask/blob/master/CHANGES.md)
/ [示例程序](https://github.com/greyli/helloflask/blob/master/demos/)
/ [HelloFlask.com](http://helloflask.com)
/ [本书主页](http://helloflask.com/book)

# FAQ

如果你想提一个问题，请创建Issue。

### 执行 flask shell 命令的时候，怎么调用 ipython，而不是默认的 Python Shell?

安装 flask-shell-ipython 库。

### 执行`pipenv install`等命令出现`TypeError`、`ResourceWarning`、或`ImportError`异常

这个是pipenv 2018.7.1版本的bug，目前可以临时通过降级pip来解决：

`$ python3 -m pip install pip==10.0.1`

如果你使用Python2，则使用下面的命令：

`$ python -m pip install pip==10.0.1`

等到新版本修复了这些问题后，可以通过下面的命令升级pipenv和pip：

```
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --upgrade pipenv
```

### 启动程序（flask run）出现`TypeError`异常

Werkzeug当前版本（14.2）存在一个Bug，当在Windows系统下使用Python2开启调试模式时，重载器会因为环境变量FLASK_ENV的编码问题而出现TypeError异常。这个Bug已在master分支修复（话说定位这个Bug花了我很长时间），预计在纸书正式发售前会发布Werkzeug 0.15版本。

目前，临时的解决方案有修改Werkzeug源码、修改python-dotenv源码、从GitHub上的master分支更新Werkzeug等，但这些方法都太麻烦。我建议你临时不开启调试模式来避免这个异常出现，也就是在.flaskenv文件中将FLASK_ENV定义那一行注释掉（使用#号），比如：

```
# FLASK_ENV=development
```
等到Werkzeug 0.15发布后，我会在知乎专栏Hello, Flask!发一篇文章通知大家更新本地依赖，并给出具体的更新方式。


### Jinja宏里为什么可以直接使用kwargs？

宏默认会自定接受额外的关键字参数，在宏内部你可以直接使用 kwargs 字典来获取这些额外的关键字参数。这里直接把这个字典传入 url_for() 函数。

顺便说一下，Jinja 宏传入关键字参数的实现有一点不太符合直觉。在定义宏的时候，并不需要传入 `**kwargs`。在宏的内部，你可以直接通过`kwargs`字典来获取所有传入的关键字参数。

也就是说，是 Jinja 自动处理这些传入的关键字参数的。另一个宏内部可以直接使用的变量是`varargs`，这个元组存储所有传入的额外位置参数，即 `*args`。


### helloflask仓库没有Git标签？

前言里在介绍Git基本用法时使用helloflask仓库作为示例，但是git tag -n命令给出位置容易产生误解。

helloflask并不包含Git标签，所以这里的命令不会输出内容。这个命令用于列出第二部分的5个项目中设置的Git标签。

### 如何通过PyCharm配置通过Flask-Script启动程序

目前不建议继续使用Flask-Script，Flask内置的CLI组件已经基本能够替代它。如果仍然要使用Flask-Scirpt，可以参考下图：

![Flask-Script在PyCharm中的启动配置](http://helloflask.com/images/pycharm-flask-script.png)

原图来自[Flask学习笔记-PyCharm配置使用Flask-Script启动以及开启Debug模式](https://my.oschina.net/ykbj/blog/618475)。

### 使用Anaconda时如何通过Pipenv创建虚拟环境

Anaconda我没用过，简单了解了一下，觉得很成熟和方便。不过，因为书中的示例程序的依赖都写在了Pipfile里，目前似乎只有Pipenv支持从Pipfile读写依赖信息（？）。Pipenv作为未来Python官方推荐的包依赖和环境管理工具，你也可以尝试一下。
这里出错通常是因为默认的Python解释器（即Anaconda内置的第三方Python发行版）和virtualenv不兼容。你可以使用下面的命令尝试一下：
```
pipenv --python /usr/local/bin/python3
```

### PyCharm无法配置运行程序，没有Module下拉选项

旧版本的PyCharm不支持通过模块来执行命令。新版本的PyCharm在图1-6的第4点位置有一个下拉选项，可以选择Module name，而不是Script。如果你使用的PyCharm没有这个下拉选项，可以通过为Python解释器选项一栏（Interpreter options）添加-m选项可以起到类似的效果，即python -m flask run。

![旧版本PyCharm配置提示](http://helloflask.com/images/pycharm-m.png)


### 为什么没有使用Flask-RESTful编写Web API？

在写作Web API这部分内容时，我考察了目前所有流行的API编写扩展，其中相对处于活跃开发状态的有[Flask-RESTful](https://github.com/flask-restful/flask-restful)、[Flask-apispec](https://github.com/jmcarp/flask-apispec)、[Flask-Classful](https://github.com/teracyhq/flask-classful)、[Flask-RestPlus](https://github.com/noirbizarre/flask-restplus)、[Flask-Restless](https://github.com/jfinkels/flask-restless)这几个。第10章的程序一开始是使用Flask-RESTful的，但后来经过再三考虑，改为单纯用Flask实现。

Flask-RESTful以及它的fork改良版Flask-RESTplus中的请求解析、响应格式化已经不推荐使用，而请求解析部分也将在未来移除，假如不使用这两部分功能，那么已经没有太大必要采用这个扩展，这是我没有使用它们的主要原因；而Flask内置的MethodView已经基本能够替代Flask-Classful，而且这个扩展看起来不太灵活；Flask-RESTless依赖于SQLAlchemy，不便于在作为一个作为示例用途的程序中使用；至于Flask-apispec，它结合了webargs和marshmallow，也提供了API文档生成功能，的确是非常好的选择，我很看好这个扩展，但是因为其刚刚出现不久，还不够完善，所以也没有选用。

### 为什么不叫REST API而使用Web API
有些读者可能不理解我为什么把常说的REST API/RESTful API说成Web API，我摘取书里的这部分内容供你参考一下：

> “仅仅通过HTTP协议返回JSON或XML数据的Web API并不能算是严格意义上的REST API。REST的提出者也在博文（http://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven）中指出不是使用了HTTP的API都叫REST API。为了避免产生混乱，本章会尽量避免REST这个词。事实上，我们不必完全按照REST的架构要求来设计API。要尽量从API的自身特点和普适的规范来设计，而不是拘泥于REST一词。”


### 执行`flask forge`命令后显示`no such command`

在部分程序中，faker被列为开发依赖，所以在安装依赖时需要添加--dev选项，即：
```
$ pipenv install --dev
```

### 第10章Todoism启动后语言切换无效

需要在启动程序前执行下面的命令生成MO文件：
```
$ flask translate compile
```
这部分内容在10.2.4详细介绍。
