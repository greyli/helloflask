# HelloFlask
A collection of Flask example applications. Repository for [*Hello, Flask!*](https://zhuanlan.zhihu.com/p/29907260).

## Demos

There are 9 applications in demos directory:

- `demos/hello`  Basic Flask application
- `demos/http`  Flask with HTTP
- `demos/template` Templating with Jinja2
- `demos/form`  Form handing with Flask-WTF (WTForms)
- `demos/database`  Database with Flask-SQLAlchemy
- `demos/email`  Send email with Flask-Mail and SendGrid
- `demos/assets`  Assets optimize with Flask-Assets
- `demos/cache`  Cache with Flask-Caching
- `demos/github-login`  GitHub OAuth login with GitHub-Flask
- and more...

## Run the demo application

Preparation work:
```
$ git clone https://github.com/greyli/helloflask.git
$ cd helloflask
$ pipenv install
$ pipenv shell
```

Run:
```
$ cd demos/hello
$ flask run
```
Now open http://localhost:5000.

You can run other application by replace `demos/hello` with proper path.

## For Chinese Readers of My Flask Book

这个仓库包含[《Flask Web开发实战》](https://zhuanlan.zhihu.com/p/29907260)第1~6章以及13章的示例程序源码。示例程序和章节的对应情况如下：

- `demos/hello`  对应第1章《初识Flask》
- `demos/http`  对应第2章《Flask与HTTP》
- `demos/template`  对应第3章《模板》
- `demos/form`  对应第4章《表单》
- `demos/database`  对应第5章《数据库》
- `demos/email`  对应第6章《电子邮件》
- `demos/assets`  对应第13章《性能优化》
- `demos/cache`  对应第13章《性能优化》

除此之外，这个仓库还包含其他Flask常见应用主题的示例程序。

## License

This project is licensed under the MIT License (see the
`LICENSE` file for details).
