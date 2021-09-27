# HelloFlask

这里是《Flask Web 开发实战》（Python Web Development with Flask）及其第二版的 Meta 仓库，包含基础示例程序源码和勘误等信息。

访问本书主页查看相关资源索引、目录、购买链接等信息：

- 第一版主页：https://helloflask.com/book/1
- 第二版主页：https://helloflask.com/book/4

P.S. 如果你阅读这本书感到有一点吃力，那么可以先翻一翻《[Flask 入门教程](https://github.com/greyli/flask-tutorial)》。


## 基础示例程序

这个仓库的 demos 和 examples 文件夹分别包含本书第一版和第二版的基础示例程序。以下为获取并运行示例程序的步骤：


### 克隆仓库

将仓库克隆到本地，然后切换进仓库根目录：

```
$ git clone https://github.com/greyli/helloflask.git
$ cd helloflask
```


### 创建虚拟环境 & 安装依赖

为了方便操作，可以把虚拟环境创建在根目录（/helloflask），让所有示例程序使用同一个环境。使用下面的命令创建虚拟环境并激活：

Windows：

```
> python -m venv env
> env\Scripts\activate
```

Linux/macOS：

```
$ python3 -m venv env
$ . env/bin/activate
```

然后安装依赖：

第一版：

```
(env) $ pip install -r requirements-v1.txt
```

第二版

```
(env) $ pip install -r requirements-v2.txt
```


### 运行示例程序

阅读示例程序目录内的 README 了解如何运行示例程序：

- 第一版：[demos/README.md](./demos/README.md)
- 第二版：[examples/README.md](./examples/README.md)


## 进阶示例程序

本书的进阶示例程序存放在独立的仓库。

第一版示例程序：

- 第 7 章示例程序（留言板）：[SayHello](https://github.com/greyli/sayhello)
- 第 8 章示例程序（个人博客）：[Bluelog](https://github.com/greyli/bluelog)
- 第 9 章示例程序（图片社交网站）[Albumy](https://github.com/greyli/albumy)
- 第 10 章示例程序（待办事项）：[Todoism](https://github.com/greyli/todoism)
- 第 11 章示例程序（聊天室）：[CatChat](https://github.com/greyli/catchat)
- 第 15 章示例程序（Flask 扩展）：[Flask-Share](https://github.com/greyli/flask-share)

第二版示例程序：

- 第 7 章示例程序（留言板）：[SayHello2](https://github.com/greyli/sayhello2)
- 第 8 章示例程序（个人博客）：[Bluelog2](https://github.com/greyli/bluelog2)
- 第 9 章示例程序（社交博客）：[WeBlog](https://github.com/greyli/weblog)


## License

该项目基于 MIT 协议授权，具体可以参考 `LICENSE` 文件。
