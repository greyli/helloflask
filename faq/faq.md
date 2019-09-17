# FAQ

如果你想提一个问题，请创建Issue。

### 第 9 章验证邮件部分，点击邮件里的验证链接无法通过验证，提示 token invalid

回退 Werkzeug 版本书中注明的 0.14.1 可解决。

### 第 6 章 Sendgrid 使用报错

在第 6 章，如果执行 sendgrid 部分的代码出现如下报错：

- `TypeError: <function Email at 0x7fce5c021e18> is not JSON serializable`
- `AttributeError：list object has no attrribute _type`
- `TypeError: __init__() got an unexpected keyword argument 'apikey'`

统一的解决方法均为回退 sendgrid-python 到书中注明的 5.3.0 版本。

### 执行 `flask run` 提示找不到程序

执行以下检查：
* 安装了所有依赖，包括开发依赖（使用 `pipenv install --dev`）
* 当前目录在项目根目录，对于第一部分的 6 个示例程序来说，切换到每个程序各自的根目录。遵循每章开头的安装命令。
* 确保没有在上层目录创建 .env 和 .flaskenv 文件。

### 执行 `flask run` 报错 `AttributeError: 'module' object has no attribute 'SSLContext'`

升级 Python 到 2.7.9 或以上版本。

### 执行 flask shell 命令的时候，怎么调用 ipython，而不是默认的 Python Shell?

安装 flask-shell-ipython 库。

### 执行`pipenv install`等命令出现`TypeError`、`ResourceWarning`、或`ImportError`异常

新版本修复了这些问题，可以通过下面的命令升级pipenv和pip：

```
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --upgrade pipenv
```

### 启动程序（flask run）出现`TypeError: environment can only contain strings`异常

使用下面的命令更新 python-dotenv 到最新版本即可解决：

```
$ pip install -U python-dotenv
```

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

> “仅仅通过HTTP协议返回JSON或XML数据的Web API并不能算是严格意义上的REST API。REST的提出者也在博文（ http://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven ）中指出不是使用了HTTP的API都叫REST API。为了避免产生混乱，本章会尽量避免REST这个词。事实上，我们不必完全按照REST的架构要求来设计API。要尽量从API的自身特点和普适的规范来设计，而不是拘泥于REST一词。”


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
