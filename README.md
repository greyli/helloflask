主页
/ [勘误](https://github.com/greyli/helloflask/blob/master/errata/errata.md)
/ [FAQ](https://github.com/greyli/helloflask/blob/master/faq/faq.md)
/ [示例程序](https://github.com/greyli/helloflask/blob/master/demos/)
/ [HelloFlask.com](http://helloflask.com)
/ [本书主页](http://helloflask.com/book)

# HelloFlask

这个仓库包含[《Flask Web开发实战》（Python Web Development with Flask）](http://helloflask.com/book)第1~6章、13章的示例程序源码和勘误信息。

你可以访问本书主页[http://helloflask.com/book](http://helloflask.com/book)查看本书的资源索引、目录、购买链接等详细信息。

# 勘误

勘误文件在[errata](https://github.com/greyli/helloflask/blob/master/errata/)目录下。

首先，为书中包含的错误表示抱歉！如果你发现了书中的错误，欢迎提交PR更新勘误文件；你也可以创建Issue指出相关错误，或是通过Email与我联系（[withlihui@gmail.com](mailto:withlihui@gmail.com)），谢谢！


## 示例程序目录

示例程序目录和章节的对应情况如下：

- `demos/hello`  对应第1章《初识Flask》
- `demos/http`  对应第2章《Flask与HTTP》
- `demos/template`  对应第3章《模板》
- `demos/form`  对应第4章《表单》
- `demos/database`  对应第5章《数据库》
- `demos/email`  对应第6章《电子邮件》
- `demos/assets`  对应第13章《性能优化》
- `demos/cache`  对应第13章《性能优化》

*在书中，每一章的开头都会包含运行实例程序的提示。*


## 运行程序

克隆仓库：
```
$ git clone https://github.com/greyli/helloflask.git
$ cd helloflask
```
安装依赖包：
```
$ pipenv install --dev --pypi-mirror https://mirrors.aliyun.com/pypi/simple
$ pipenv shell
```
*如果你还没有安装Pipenv，那么可以在运行`pipenv`命令前通过pip安装（`pip install pipenv`）。*

运行实例程序：
```
$ cd demos/hello
$ flask run
```
现在使用浏览器打开http://localhost:5000

你可以通过切换到不同的示例程序目录来运行不同章节的示例程序。比如，下面的命令将会运行第4章的示例程序：
```
$ cd demos/form
$ flask run
```

## 相关项目

* [SayHello](https://github.com/greyli/sayhello)： 本书第7章示例程序，一个简单的留言板程序。
* [Bluelog](https://github.com/greyli/bluelog)：本书第8章示例程序，一个个人博客。
* [Albumy](https://github.com/greyli/albumy)：本书第9章示例程序，多人图片社交网站。
* [Todoism](https://github.com/greyli/todoism)：本书第10章示例程序，实现了Web API和i18n支持的Todo程序。
* [CatChat](https://github.com/greyli/catchat)：本书第11章示例程序，基于WebSocket实现，并提供了社交账户登录功能的聊天室。
* [Flask-Share](https://github.com/greyli/flask-share)：本书第15章的Flask扩展示例。

## License

该项目基于MIT协议授权，具体可以参考`LICENSE`文件。
