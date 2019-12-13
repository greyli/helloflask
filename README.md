# HelloFlask

这里是《Flask Web开发实战》（Python Web Development with Flask）的Meta仓库，包含第1-6章、13章的示例程序源码和勘误等信息。访问[本书主页](http://helloflask.com/book)查看本书的资源索引、目录、购买链接等详细信息。

## Resources

* [阅读勘误表](http://helloflask.com/book/errata)（优化格式后便于阅读的勘误表）
* [FAQ](https://github.com/greyli/helloflask/blob/master/faq/faq.md)（常见问题）
* [可改进实现](https://github.com/greyli/helloflask/blob/master/improvement/improvement.md)（可改进的内容描述或代码实现）
* [版本更新记录](https://github.com/greyli/helloflask/blob/master/CHANGES.md)（电子书与实体书版本更新与改进记录）

## Feedback

欢迎在本书的[豆瓣图书页面](https://book.douban.com/subject/30310340/)、对应的[知乎问题](https://www.zhihu.com/question/296048455)或是电商网站撰写评价。

如果你发现了书中的错误、运行实例程序出错或是有其他的问题，可以[创建Issue](https://github.com/greyli/helloflask/issues/new/)或是在 [HelloFlask 论坛](https://discuss.helloflask.com)发帖进行反馈。

## Demos

这个仓库的 demos 文件夹包含本书第一部分的示例程序，每一章对应一个文件夹。使用下面的步骤运行示例程序。

克隆仓库：
```
$ git clone https://github.com/greyli/helloflask.git
$ cd helloflask
```
创建&激活虚拟环境并安装依赖包（下面两种方式二选一）：

Option 1 使用 venv/virtualenv + pip：
```
$ python -m venv env  # Python 2 使用 virtualenv env 命令
$ source env/bin/activate  # Windows 使用 env\Scripts\activate 命令
$ pip install -r requirements.txt
```

对于上面的命令，根据你安装的 Python 版本和所在操作系统选用 `python` 或 `python3`，`pip` 或 `pip3`。

Option 2 使用 Pipenv：
```
$ pipenv install --dev
$ pipenv shell
```
如果你还没有安装Pipenv，那么可以在运行`pipenv`命令前通过pip安装（`pip install pipenv`）。

运行示例程序（以第一章示例程序为例）：
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

*在书中，每一章的开头都会包含运行实例程序的提示。*

## HelloFlask Projects

* [SayHello](https://github.com/greyli/sayhello)： 本书第7章示例程序，一个简单的留言板程序。
* [Bluelog](https://github.com/greyli/bluelog)：本书第8章示例程序，一个个人博客。
* [Albumy](https://github.com/greyli/albumy)：本书第9章示例程序，多人图片社交网站。
* [Todoism](https://github.com/greyli/todoism)：本书第10章示例程序，实现了Web API和i18n支持的Todo程序。
* [CatChat](https://github.com/greyli/catchat)：本书第11章示例程序，基于WebSocket实现，并提供了社交账户登录功能的聊天室。
* [Flask-Share](https://github.com/greyli/flask-share)：本书第15章的Flask扩展示例。

## License

该项目基于MIT协议授权，具体可以参考`LICENSE`文件。
