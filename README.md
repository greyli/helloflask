主页
/ [勘误](https://github.com/greyli/helloflask/blob/master/errata/errata.md)
/ [FAQ](https://github.com/greyli/helloflask/blob/master/faq/faq.md)
/ [可改进实现](https://github.com/greyli/helloflask/blob/master/improvement/improvement.md)
/ [版本更新记录](https://github.com/greyli/helloflask/blob/master/CHANGES.md)
/ [示例程序](https://github.com/greyli/helloflask/blob/master/demos/)
/ [HelloFlask.com](http://helloflask.com)
/ [本书主页](http://helloflask.com/book)

# HelloFlask

这里是[《Flask Web开发实战》（Python Web Development with Flask）](http://helloflask.com/book)的Meta仓库，包含第1-6章、13章的示例程序源码和勘误等信息。

你可以访问本书主页[http://helloflask.com/book](http://helloflask.com/book)查看本书的资源索引、目录、购买链接等详细信息。

本书相关项目的源码建议你按照书中的指导使用Git克隆到本地，如果克隆速度过慢，可以点击<a href="http://helloflask.com/downloads/helloflask-projects-18-8-29.zip" target="_blank" download>这里</a>下载源码合集文件。

## 勘误 & FAQ & 可改进实现 & 版本更新记录

* [勘误](https://github.com/greyli/helloflask/blob/master/errata/errata.md)（书中的笔误、错误及排版问题等）
* [FAQ](https://github.com/greyli/helloflask/blob/master/faq/faq.md)（常见问题）
* [可改进实现](https://github.com/greyli/helloflask/blob/master/improvement/improvement.md)（可改进的内容描述或代码实现）
* [版本更新记录](https://github.com/greyli/helloflask/blob/master/CHANGES.md)（电子书与实体书版本更新与改进记录）

首先，为书中包含的错误表示抱歉！如果你发现了书中的错误/常见问题/可改进实现，欢迎提交PR更新上述链接指向的文件；你也可以[创建Issue](https://github.com/greyli/helloflask/issues/new/choose)指出相关事项，或是通过Email与我联系（[withlihui@gmail.com](mailto:withlihui@gmail.com)），谢谢！

## 问题反馈

如果你发现了书中的错误、运行实例程序出错或是有其他的问题，可以[创建Issue](https://github.com/greyli/helloflask/issues/new/choose)进行反馈。

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


## Powered by This Book

如果你通过阅读本书实现了自己的小项目，欢迎通过各种途径让我知道，我会把你的项目添加到这里和本书主页。


## 分享 & 评价

如果这本书帮到了你，或是你觉得这本书还不错，欢迎通过社交平台私信或是或发Email告诉我，这对我来说是非常珍贵的鼓励！

另外，你也可以通过下面的途径来分享和推荐本书：

* 直接向朋友或同事推荐
* 在新浪微博、Twitter或知乎等平台分享并@我（新浪微博@李辉Grey，Twitter@greylihui，知乎@李辉）
* 在你的博客或其他平台写文章分享你的阅读心得
* 在本书的[豆瓣图书页面](https://book.douban.com/subject/30310340/)写短评或书评
* 在知乎问题“[如何评价《Flask Web开发实战》](https://www.zhihu.com/question/296048455)？”下撰写答案
* 在知乎问题“[《Flask Web开发实战》中有哪些有趣的细节和彩蛋？](https://www.zhihu.com/question/296047204)”下撰写答案
* 在本书的京东、亚马逊、当当商品页面写评价


## License

该项目基于MIT协议授权，具体可以参考`LICENSE`文件。
