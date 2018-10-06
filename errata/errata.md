[主页](https://github.com/greyli/helloflask)
/ 勘误
/ [FAQ](https://github.com/greyli/helloflask/blob/master/faq/faq.md)
/ [可改进实现](https://github.com/greyli/helloflask/blob/master/improvement/improvement.md)
/ [版本更新记录](https://github.com/greyli/helloflask/blob/master/CHANGES.md)
/ [示例程序](https://github.com/greyli/helloflask/blob/master/demos/)
/ [HelloFlask.com](http://helloflask.com)
/ [本书主页](http://helloflask.com/book)

# 勘误

下面是《Flask Web开发实战》的勘误信息。我在helloflask.com上创建了一个镜像勘误页面，阅读体验更好，请访问 http://helloflask.com/book/errata 查看。

最后更新：2018/10/6

## 贡献指南

如果你发现了书中的错误，欢迎提交PR更新勘误文件；你也可以创建Issue指出相关错误，或是通过Email与我联系（[withlihui@gmail.com](mailto:withlihui@gmail.com)），谢谢！

创建PR时，请参考下列要求：

* 勘误需要按照章节顺序排列，全局错误放到最上面。
* 每一列的内容说明参考如下：

章节 | 页码 | 位置 | 错误文字 | 正确文字 | 备注 | 发现时间 |
--- | --- | --- | --- | --- | --- | ---
| 所在章节，比如1.3.2 | 纸书页数 | 所在位置，比如第X行 | 错误的文字内容 | 修改正确的文字内容 | 额外的备注信息，比如错误类别，或是你的牢骚 | 发现时间，格式为18.9.10 |

错误分类说明：

* 笔误：错别字（包括中文和英文），也可以细分为拼写错误、大小写错误，同时包括代码中漏掉某个符号之类的错误
* 错误：描述错误、代码错误
* 审校错误：编辑后期修改和审校中引入的错误
* 排版错误：排版人员引入的错误

*因为电子书因为尺寸不同，会产生不同的页数，这里的勘误页码为纸书页码，电子书可以根据章节和位置来定位错误内容。*


## 纸书

纸书的版本号格式为“版本号-印次号”，“1-1”即“第一版第一次印刷”。**每一次重印会修正上一印次包含的所有错误**，版本号可以在版权页看到。

### 1-1

发布时间：2018/9/1

章节 | 页码 | 位置 | 错误文字 | 正确文字 | 备注 | 发现时间 |
--- | --- | --- | --- | --- | --- | ---
| 全局 | - | -  | 单击 | 点击 | 审校错误。多处。编辑称这个修改是出版社的规范要求，我觉得有些莫名其妙 |
| 全局 | - | -  |  | 代码块中的英文单词换行被截断时错误的添加的连接线 | 排版错误。多处，详情见下面的列表 |
| 全局 | - | -  | Github | GitHub | 大小写错误。多处 |
| 前言 | V | 本书主要特点中的第2点 | 第一部分的2~6章 | 第一部分的1~6章 | 审校错误 |
| 前言 | V | 本书主要特点中的第3点 | Pyhton | Python | 拼写错误 |
| 前言 | V | 本书主要特点中的第3点 | Boostrap | Bootstrap | 审校错误 |
| 前言 | X | 排版约定最后一段的上面1行 | you_email| your_email | 拼写错误 |
| 1.2 | P11 | 代码清单1-1下的提示文字 | 命令为 | 命名为 | 笔误 |
| 1.2.2.2 | P13 | 第1个附注文字下第2行 | http://helloflask.com/hello/Grey | http://helloflask.com/greet/Grey | 笔误 |
| 1.3.1 | P14 | 标题 | Run，Flask，Run！  | Run, Flask, Run! | 标点错误 |
| 1.3.1 | P14 | 第1个代码块最后1行 | | 出现多余的缩进 | 排版错误 |
| 1.3.1.3 | P17 | 配置步骤4 | 下列选项 | 下拉选项 | 笔误 |
| 1.3.3 | P18 | 第1行 | Enviroment  | Environment | 拼写错误 |
| 1.7 | P23 | 第2个代码块下第1行 | `url_for('say_hello', name='Jack')` | `url_for('greet', name='Jack')` | 笔误 |
| 2.2.3 | P34 | 图2-5 |  | 地址栏的地址应为/nothing，和描述对应。图中的/foo在后面实际被定义了 | 笔误 | 18.9.28 |
| 2.2.3.3 | P36 | 第1个代码块 | `'goback/<int:year>'` | `'/goback/<int:year>'` | 笔误。URL规则漏掉了开头的斜线 | 18.9.28 |
| 2.3.1 | P40 | 第3个代码块 | `{'Location', 'http://www.example.com'}` | `{'Location': 'http://www.example.com'}` | 笔误。返回值中字典里的符号出错 |
| 2.3.2 | P44 | HTML小节的最后1行 | HTTP | HTML | 笔误 |
| 2.3.3 | P47 | 第2个附注段落 | Respone | Response | 笔误。拼写错误 |
| 2.5.4.1.(3) | P67 | 第1个代码块 | `db.execute('SELECT * FROM students WHERE password=?, password)` | `db.execute('SELECT * FROM students WHERE password=?', password)` | 笔误。字符串漏写右侧关闭引号 |
| 3.1 | P77 | 代码清单3-1下的提示 | HTML5 | HTML | 多余文本。另外，后面的链接需要更新为https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure |
| 3.3.2 | P89 | 第2段文字中 | _macors.html | _macros.html | 笔误 |
| 3.4.4 | P101 | 图3-5 | | 地址栏的地址应为/nothing，和描述对应。 | 笔误 | 18.10.1 |
| 4.2.3 | P110 | 代码清单4-2最后1行 | `'login.html'` | `'basic.html'` | 笔误 | 18.9.28 |
| 4.3.1 | P112 | 第1个代码块后第1行 | 3000 | 2000 | 笔误，不同的浏览器对于URL有不同的长度限制，此处的长度为“最佳实践” |
| 4.3.3 | P117 | 代码清单4-7第4行 | `form.username()` | `form.username` | 笔误。此处的括号可有可无，去掉以保持风格上的统一 | 18.9.24 |
| 4.4.4.1 | P123 | 代码清单4-13第1行 | `flask wtf` | `flask_wtf` | 审校错误 | 18.9.24 |
| 5.4.1.1 | P147 | 第1个代码块第4行 | `'DON'T BELIEVE……'` | `'DON\'T BELIEVE……'` | 代码错误，字符串漏掉了转义符号 |
| 5.4.1.2 | P150 | 表5-7下的第1个代码块 | `Note.body='SHAVE'` | `Note.body == 'SHAVE'` | 代码错误，少了1个等于号 | 18.9.22 |
| 5.5.2.4 | P162 | 代码清单5-11第8行 | `title = ` | `name = ` | 笔误 | 18.9.26 |
| 5.5.2.4 | P163 | 第3个代码块第6行 | `it.writer = writer` | `it.writer = king` | 笔误 | 18.9.26 |
| 5.5.3 | P164 | 代码清单5-13上面 | 都定义在“多”这一侧，即City类中 | 都定义在“多”这一侧，即Citizen类中 | 笔误 |
| 5.5.4 | P165 | 第2个代码块第6行 | - | 第6行`>>> china.capital = beijing`移动到第3行 | 笔误 |
| 5.5.4 | P165 | 第2个代码块第8行 | `<Capital 1>` | `<Capital u'Beijing'>` | 笔误 |
| 5.5.4 | P166 | 第2个代码块第10行 | `u'China'` | `<Country u'China'>` | 笔误 |
| 5.5.4 | P166 | 第2个代码块第11行 | `name'Tokyo'` | `name='Tokyo'` | 笔误 | 18.9.26 |
| 5.7.1.2 | P174 | 最后1个代码块第1行 | `Post.quer2y.get(2)` | `Post.query.get(2)` | 审校错误。 |
| 5.7.2 | P176 | 代码清单5-18下第1行 | targe | target | 笔误 | 18.9.28 |
| 5.7.2 | P177 | 最后1个代码块上面 | 参数name | 参数named | 笔误 | 18.9.28 |
| 5.7.2 | P177 | 最后1段提示文字 | 监听函数时， | 监听函数。这时 | 审校错误 | 18.9.28 |
| 5.7.2 | - | 全章节多处 | listen_for | listens_for | 笔误 | 18.9.28 |
| 5.8 | P177 | 最后1行 | 本章要介绍的 | 本章介绍的 | 笔误 | 18.9.28 |
| 7.2.3.1 | P202 | 代码清单7-3的文件路径 | sayhello.py | models.py | 笔误 |
| 7.3.2 | P208 | 第1个代码块第6行 | `render_form(form),action=request.full_path` | `render_form(form, action=request.full_path)` | 审校错误，右侧关闭括号位置出错 |
| 7.3.2 | P208 | 表7-2上面段落的最后一句话 | quick_form() | render_form() | 笔误。历史遗留问题 | 18.9.28 |
| 8.1 | P220 | 文件目录树 | | 目录树漏掉了 __init__.py 文件 | 笔误。 | 18.10.1 |
| 8.1.3 | P229 | 第2个提示段落 | 新创建的模块 | 新创建模块 | 审校错误。 | 18.9.24 |
| 8.3.1 | P252 | 第1个代码块最后1行 | `'index.html'` | `'blog/index.html'` | 笔误 | 18.10.06 |
| 8.3.1 | P252 | 代码清单8-24文件路径 | templates/index.html | templates/blog/index.html | 笔误 | 18.10.06 |
| 8.3.5 | P263 | 第1个代码块第6行 | `Comment.query.with_parent(post)` | `Comment.query.with_parent(post).filter_by(reviewed=True)` | 笔误 | 18.9.26 |
| 8.3.7 | P267 | 代清清单8-31第4行 | `comment.photo_id` | `comment.post_id` | 笔误 | 18.9.26 |
| 8.3.7 | P267 | 代清清单8-31下方正文第2段最后一行的URL中 | photo | post | 笔误 | 18.9.26 |
| 8.7.2.1 | P293 | 第1个代码块下面的提示文字 | HTmL | HTML | 审校错误，大小写错误 |
| 8.2.1.1.(4) | P235 | 第2个代码块第3行 | `db.relationship('Comment', backref='post', cascade='all')` | `db.relationship('Comment', back_populates='post', cascade='all, delete-orphan')` | 笔误 |
| 10.2.5 | P438 | 标题上面的附注文字 | 生成帮助信息 | 生成的帮助信息 | 审校错误。编辑以为自己在改病句，实际上却是在制造病句 |
| 10.3.1.4 | P443 | 最后1段第5行 | RSET | REST | 笔误 |
| 10.3.3.5 | P453 | 最后1行 | flask-restless | Flask-Restless | 大小写错误 |
| 10.3.6.3 | P468 | 第1行 | app.error_handler | app.errorhandler | 笔误 |
| 11.4.3.5 | P503 | 代码清单11-11中多处 | `get['XXX']` | `get('XXX')` | 审校错误 |
| 11.5.1 | P509 | 代码清单11-13第5行 | `position === 0&& socket.nsp` | `position === 0 && socket.nsp` | 审校错误。空格缺失 |
| 12.3.2 | P527 | 代码清单12-2第7行 | test_app_exsit | test_app_exist | 拼写错误 |
| 14.4.2 | P574 | 第2个提示段落上面 | python(3)两处 | python3 | 审校错误 |
| 15.7.3 | P625 | 最后1个代码块的第2行 | `git push origm` | `git push origin` | 审校错误。另外，这一行下面的Github应为GitHub |


断行单词在排版时产生的错误连字符位置列表：

* 9.4.1第2个代码块
* 9.5.2代码清单9-16
* 10.3.4代码清单10-17第1行

关于URL长度限制的详情可以参考[WWW FAQs: What is the maximum length of a URL?](https://www.boutell.com/newfaq/misc/urllength.html)。

## 电子书

此处列出电子书特有的错误，多为排版错误，其他通用勘误请参考上面的纸书勘误。

### 2018/8/24版本

章节 | 页码 | 位置 | 错误文字 | 正确文字 | 备注 |
--- | --- | --- | --- | --- | ---
| 全局 | - | -  | （） | () | 排版错误。所有半角括号被改为全角括号 |
| 全局 | - | -  | `foo--bar` | `foo --bar` | 排版错误。多处。比如`flask --help`被错误写为`flask--help` |
| 第5章 | - | - | `flaskinitdb` | `flask initdb` | 排版错误。命令间的空格缺失 |

*更新：电子书中上述错误已经修正并发送给各大平台，请联系客服进行更新。*

### 2018/9/10版本

章节 | 位置 | 错误文字 | 正确文字 | 备注 |
--- | --- | --- | --- | ---
| 1.5.1 | 第1个提示文字 | `python-m` | `python -m` | 排版错误。空格缺失 |
| 12.5.2 | 第2个代码块下 | `coverage run-m` | `coverage run -m` | 排版错误。空格缺失 |

另外，此版本还完善了目录，添加了三级标题，跳转更加方便。

*更新：电子书中上述错误已经修正并发送给各大平台，请联系客服进行更新。*

## 源码错误

此处列出书中没有涉及的程序代码错误，目前临时在master分支更新，后续会重写相应的标签。

程序 | 描述 | commit | 备注 |
--- | --- | --- | ---
| Albumy | Albumy评论模板中的用户头像应该使用中等尺寸，即`avatar_m` | [4c6622c](https://github.com/greyli/albumy/commit/4c6622cc30377ebf2e1da64f570de71ddcc522d2) |  |
| Albumy | 图片详情页上的开启/关闭评论按钮应该使用表单实现，提交POST请求 | [4ef2898](https://github.com/greyli/albumy/commit/4ef28988586fc09a64e31b87722b83615416b1cd) | 由[Shimada666](https://github.com/Shimada666)发现 |
| CatChat | 删除用户功能时的删除按钮的class写错了，而且JavaScript中的事件函数需要监听document | [c264aac](https://github.com/greyli/catchat/commit/c264aac6fd35f527e0bd461b88fa05ab207b55f2) |  |

## 新变化提示

* 第1章：PyCharm 2018.2版本增加了对Pipenv的支持。
* 第1章：Pipenv自2018.7.1版本后在Windows中激活虚拟环境后会显示虚拟环境提示符（具体版本号待确认）。
* 第15章中的Flask-Share源码对应0.1.0版本。
