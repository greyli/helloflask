# HelloFlask

Flask书[《Flask Web开发实战》（Python Web development with Flask）](http://helloflask.com/book)仓库。

## 包含内容
这个仓库包含[《Flask Web开发实战》](http://helloflask.com/book)第1~6章、13章的示例程序源码和勘误信息。


示例程序目录和章节的对应情况如下：
- `demos/hello`  对应第1章《初识Flask》
- `demos/http`  对应第2章《Flask与HTTP》
- `demos/template`  对应第3章《模板》
- `demos/form`  对应第4章《表单》
- `demos/database`  对应第5章《数据库》
- `demos/email`  对应第6章《电子邮件》
- `demos/assets`  对应第13章《性能优化》
- `demos/cache`  对应第13章《性能优化》

勘误文件在`errata`目录下。


## 运行程序

克隆仓库，并安装依赖包：
```
$ git clone https://github.com/greyli/helloflask.git
$ cd helloflask
$ pipenv install
$ pipenv shell
```
如果你还没有安装Pipenv，那么可以在运行`pipenv`命令前通过`pip install pipenv`来安装。
```
$ cd demos/hello
$ flask run
```
现在使用浏览器打开http://localhost:5000即可看到示例程序主页。

你可以通过切换到不同的示例程序目录来运行不同的程序，比如，下面的命令将会运行第4章的示例程序：
```
$ cd demos/form
$ flask run
```
在书中，每一章的开头都会包含运行实例程序的提示。


## License

该项目基于MIT协议授权，具体可以参考`LICENSE`文件。
