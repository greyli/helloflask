# 获取示例程序

这个仓库的 [demos](https://github.com/greyli/helloflask/tree/master/demos) 和 [examples](https://github.com/greyli/helloflask/tree/master/examples) 文件夹分别包含《Flask Web 开发实战》第 1 版和第 2 版的基础示例程序。以下为获取并运行示例程序的步骤：


## 克隆仓库

将仓库克隆到本地，然后切换进仓库根目录：

```
$ git clone https://github.com/greyli/helloflask.git
$ cd helloflask
```

## 创建虚拟环境 & 安装依赖

为了方便操作，可以把虚拟环境创建在仓库根目录（/helloflask），让所有示例程序使用同一个环境。

=== "第 2 版（PDM）"

    首先[安装 PDM](https://pdm-project.org/latest/#installation)：

    ```
    pip install --user pdm
    ```

    然后使用 PDM 安装依赖并创建虚拟环境：

    ```
    pdm install --dev
    ```

=== "第 2 版（pip）"

    使用下面的命令创建虚拟环境并激活：

    Windows：

    ```
    python -m venv .venv
    .venv\Scripts\activate
    ```

    Linux/macOS：

    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    然后安装依赖：

    ```
    (.venv) $ pip install -r requirements/v2.txt
    ```

=== "第 1 版（Pipenv）"


    首先[安装 Pipenv](https://pipenv.pypa.io/en/latest/installation.html)：

    ```
    pip install --user pipenv
    ```

    然后使用 Pipenv 安装依赖并创建虚拟环境：

    ```
    $ pipenv install --dev
    ```

=== "第 1 版（pip）"

    使用下面的命令创建虚拟环境并激活：

    Windows：

    ```
    python -m venv .venv
    .venv\Scripts\activate
    ```

    Linux/macOS：

    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    然后安装依赖：

    ```
    (.venv) $ pip install -r requirements/v1.txt
    ```

## 运行示例程序

阅读不同版本对应的示例程序文档了解详细运行操作：

- [第 1 版](book/1/example.md)
- [第 2 版](book/4/example.md)


## 进阶示例程序

本书第二部分的示例程序存放在独立的仓库，安装步骤见各自项目的 GitHub 主页。目录索引见[示例程序索引](https://github.com/greyli/helloflask#examples)。
