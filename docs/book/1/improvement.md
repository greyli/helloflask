# 可改进的实现

下面是《Flask Web开发实战》的可改进实现。书中的第二部分的程序编写时需要同时写作书稿，时间上比较仓促，没有深入思考程序的设计与实现。

如果你发现了书中的可改进实现，欢迎提交PR更新可改进实现文件；你也可以创建Issue指出相关问题，或是通过Email与我联系（[withlihui@gmail.com](mailto:withlihui@gmail.com)），谢谢！

这个文件的编写模式还有待确定，欢迎各种有益的探索。

## 文本描述与章节安排等

### 第1章Pipenv相关介绍

* 加入使用第三方PyPI源的方法介绍，包括修改Pipfile、通过环境变量设置以及通过命令行选项设置。
* 增加对旧版本PyCharm启动配置的说明。
* pipenv update 命令会更新所有依赖包，等待这个行为改变，或添加提示在第 7 页。

### 第1章和第8章对于FLASK_APP合法值的描述

第一章介绍FLASK_APP时1.3.1.1（P15）添加描述：FLASK_APP的值是模块所在的“路径“。并介绍几种合法的可选值，可以参考文档：

> FLASK_APP has three parts: an optional path that sets the current working directory, a Python file or dotted import path, and an optional variable name of the instance or factory. If the name is a factory, it can optionally be followed by arguments in parentheses. The following values demonstrate these parts:

> 来源：http://flask.pocoo.org/docs/1.0/cli/#application-discovery

同时更新第8章8.1.3（P232）中的两处措辞（均改为“导入路径”）：
* 第一段的“模块中”
* 注意段落中的“包中”

### 第2章的any转换器

这里可以添加一个提示，当需要给出数字作为选项时，需要添加引号将数字作为字符串，以便正确作为正则表达式匹配：

```py
@app.route("/number/<any('1', '2', '3'):num>")
def choose_a_number():
    ...
```

### 第3章介绍宏的部分添加关于kwargs和varargs的提示

这部分内容容易让人疑惑，书中没有详细介绍它们，详情见FAQ中相关问题。

### 第 5 章

* 表 5-2 下面简单介绍 URI 的格式，添加对 MySQL 使用不同 Python 接口库的 URI 变化说明。 

### 第14章部署后更新程序添加说明

14.4.8添加一个小提示，提示可以直接使用`supervisorctl restart`命令。确认两者的区别，顺便添加reload的说明。

## 程序设计与实现

### Albumy

#### 9.4.3 写入用户权限中的角色与权限字典的设计

* 相关Issue：https://github.com/greyli/albumy/issues/1
* 贡献者：@[AngelLiang](https://github.com/AngelLiang)
* 主要描述：「代码应尽量完全表达设计者的思路」。在设计角色和权限字典时，虽然Guest和Blocked用户没有任何权限，但是应在代码中有所体现，所以此处应该添加注释：

```py
roles_permissions_map = {
    # 'Guest': [],
    # 'Blokced': [],
    'Locked': ['FOLLOW', 'COLLECT'],
    'User': ['FOLLOW', 'COLLECT', 'COMMENT' 'UPLOAD'],
    'Moderator': ['FOLLOW', 'COLLECT', 'COMMENT', 'UPLOAD', 'MODERATE'],
    'Administrator': ['FOLLOW', 'COLLECT', 'COMMENT', 'UPLOAD', 'MODERATE', 'ADMINISTER']
}
```

### 关于发送验证邮件的设计

目前更合理的主流设计是注册的时候不发确认邮件，等用户自行登录后，显示提示需要确认邮件，用户点击发送邮件按钮后再发送邮件。


### 禁止锁定和封禁协管员和管理员

* 相关 Issue： https://github.com/greyli/albumy/issues/7
* 相关 Commit： https://github.com/greyli/albumy/commit/943829b819b7bda6921d6c0fe277c75cd6a98033
* 主要描述：在用户后台管理，不对管理员和协管员显示封禁锁定按钮，同时在对应视图进行检查。

以锁定为例，原代码：
```py
user.lock()
flash('Account locked.', 'info')
```
修改为：
```py
if user.role.name in ['Administrator', 'Moderator']:
    flash('Permission denied.', 'warning')
else:
    user.lock()
    flash('Account locked.', 'info')
```
封禁处理类似。模板中处理类似。

### bluelog

#### 虚拟数据中相关代码的优化

* 相关Issue：https://github.com/greyli/bluelog/issues/1
* 贡献者：@[AngelLiang](https://github.com/AngelLiang)
* 主要描述：「尽量使虚拟数据接近真实的数据」。虚拟数据中生成的评论时间应该晚于文章时间，评论回复时间应该晚于评论时间，并且评论和回复应关联同一篇文章。不过由于虚拟数据主要目的是展示或测试视觉效果，所以不必把太多精力放在这里。

### 主页评论数量改进

https://github.com/greyli/bluelog/issues/3

### CatChat

### 删除用户后的操作优化

当前实现中，删除用户后仅会弹出提示，但是因为页面没有更新，被删除用户的消息仍然在消息列表中。有两种可行的优化方法：

* 提示中添加“请刷新页面”。
* 在删除成功的回调函数中重载页面。
* 定位所有该用户在页面上的消息元素，动态去除。

## 排版、风格设计

### 每一部分开头配图

可以有下面的改进：

* 每一部分开头的Flask图片我曾要求编辑将其缩小放到右上角，但是电子版没有调整，结果图片太大了，大到能够看清我蹩脚处理后留下的锯齿。
* 自己画这几个图片，去掉版权声明。

### 封面配图

* 封面的图片颜色和设计图相比有些失真，需要完善。
* 图片可以再大一点。

## 第 1 版第 4 次印刷（2019/7/1）更新

下面的内容已经在 1-4 版本中修正。

* P583页最下方段落删除和 P581页倒数第二段重复的部分。
* 117页，4.3.3的第二小段，“像第2章渲染flash()消息一样”修正为是“像第3章渲染flash()消息一样”。
* 修改第 8 章描述现实配置部分，邮箱服务器配置通常是写在配置文件里的。
* 7.4.5 P211 示例代码中的 `timestamp` 改为 `message.timestamp`，这样更容易理解。

### Bluelog 管理字数统计

详情见 https://github.com/greyli/bluelog/issues/9

### SayHello 视图函数代码优化

* 相关Issue：https://github.com/greyli/sayhello/issues/4
* 贡献者：@[realzhangm](https://github.com/realzhangm)

一个视图，如果同时处理 GET 和 POST 请求，那么对于 POST 请求用不到的代码，可以放到 POST 请求的 if 语句块下面执行，以减少不必要的调用。以 SayHello 为例：

```py
@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    # ... 原来的位置
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    messages = Message.query.order_by(Message.timestamp.desc()).all()  # 优化后的位置
    return render_template('index.html', form=form, messages=messages)
```

## 第 1 版第 3 次印刷（2019/4/1）更新

下面的内容已经在 1-3 版本中修正。

### 关于导入语句

为了节省篇幅，除非是第一次出现的类和函数等接口，导入语句都省略掉了。对于某些交互式代码块，添加必要的导入语句会更友好。包含下面这些：

7.5 P214 代码清单7-8：
```py
from sayhello import db
from sayhello.models import Message
```

8.2.1 P237 代码清单8-10
```py
import random
```

### 第 5 章

* 表 5-6 get() 等方法接受的参数 ident 改为 id。
* 表 5-7 第一列的标题改为“过滤方法”。

### 第 6 章 

* 6.1.1 P181 代码清单6-1 第 9-13 行参数对去掉等号两边的空格。

### 第 8 章

P275 该小节最后添加一段提示文字：

提示 在 fakes.py 脚本里的 fake_admin() 函数中，我们需要在 admin 对象创建后，为虚拟用户记录设置密码，添加后面的代码：admin.set_password('helloflask')。

### 第3章3.3.2最后的两个列表

* 相关Issue：https://github.com/greyli/helloflask/issues/26
* 贡献者：@[BobcatsII](https://github.com/BobcatsII)

描述中使用了“第一个列表的2、3、4项”的表达，为了更好的定位，这里的两个列表应该使用有序标号。1-2 版本反馈给编辑，但是没有改，或许可以把这句改为“上面第一个列表的第2、3、4项”。

## 第 1 版第 2 次印刷（2019/1/1）更新

下面的内容已经在 1-2 版本中修正。

### 前言和附录中的勘误URL

GitHub上的勘误文件阅读体验不太好，而且部分地区访问较慢，我在helloflask创建了一个镜像勘误页面，可以将前言和附录中的勘误URL改为 http://helloflask.com/book/errata 。

### 介绍Git标签部分容易产生误解

在前言中介绍Git基本用法中的列出Git标签部分时，因为作为示例的helloflask并没有包含Git标签，所以这里容易产生误解，应该添加一个说明。

### 完善导入

6.2.3.1 P186 “创建发信对象”下面的第 1 个代码块，在最前插入一行：
```py
>>> import os
```

### 第1章Pipenv相关介绍

* 去掉在Windows中执行pipenv shell激活虚拟环境不显示环境提示信息的段落。
* PyCharm从2018.2版本起提供了对Pipenv的支持，第一章相关内容可以进行改写。


### 第3章空白控制示例代码

这部分示例代码逻辑上不正确，3.4.1 P93 部分的4个代码块依次需要更改为：

```html
<div>
{% if True %}
    <p>Hello!</p>
{% endif %}
</div>
```

```html
<div>

    <p>Hello!</p>

</div>
```

```html
<div>
{% if True -%}
    <p>Hello!</p>
{%- endif %}
</div>
```

```html
<div>
    <p>Hello!</p>
</div>
```

### 第3章3.2.5中关于自定义环境的描述

第一个注意段落下的这句“这通过向对应的字典属性中添加一个键值对实现，传入模板的名称作为键，对应的函数对象或变量作为值。”

其中的“传入模板的名称作为键”，可以补全前面隐藏的动词，从而避免误解，即“使用传入模板的名称作为键”。


### 第10章开头的启动命令

在本章开头给出的初始化命令应该加入`flask translate compile`，以便生成MO文件，让程序中的语言切换生效。因为这个命令对应的内容在10.2.4，这里可以添加一句提示。


### 后记

拿到书才发现，编辑把我的后记删掉了。因为成本问题，临时妥协的解决方法是在重印时稍加修改后放到前言最后的空白处。尽管如此，还是希望有机会添加一个后记。（在 1-2 版本改为放到前言最后的空白处。）
