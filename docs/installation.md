# 获取示例程序

这个仓库的 [demos](https://github.com/greyli/helloflask/tree/master/demos) 和 [examples](https://github.com/greyli/helloflask/tree/master/examples) 文件夹分别包含《Flask Web 开发实战》第 1 版和第 2 版的基础示例程序。以下为获取并运行示例程序的步骤：


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

第 1 版：

```
(env) $ pip install -r requirements/v1.txt
```

第 2 版

```
(env) $ pip install -r requirements/v2.txt
```


### 运行示例程序

阅读不同版本对应的示例程序文档了解详细运行操作：

- [第 1 版](/book/1/example)
- [第 2 版](/book/4/example)


## 进阶示例程序

本书第二部分的示例程序存放在独立的仓库，安装步骤见各自项目的 GitHub 主页。目录索引见[示例程序索引](/examples)。
