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

最后更新：2018/11/18

## 贡献指南

如果你发现了书中的错误，欢迎提交PR更新勘误文件；你也可以创建Issue指出相关错误，或是通过Email与我联系（[withlihui@gmail.com](mailto:withlihui@gmail.com)），谢谢！

创建PR时，请参考下列要求：

* 勘误需要按照章节顺序排列，全局错误放到最上面。
* 每一列的内容说明参考如下：

章节 | 页码 | 位置 | 错误文字 | 正确文字 | 备注 | 发现时间 |
--- | --- | --- | --- | --- | --- | ---
| 章节号 | 纸书页数 | 以章节出发的位置描述 | 错误的文字内容 | 修改正确的文字内容 | 额外的备注信息，比如错误类别，或是你的牢骚 | 发现时间，格式为YY.M.DD |

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

#### 重要勘误

此处的勘误为会影响程序运行和理解的错误，需要在阅读前标记到书上，以免影响阅读。

章节 | 页码 | 位置 | 错误文字 | 正确文字 | 备注 | 发现时间 |
--- | --- | --- | --- | --- | --- | ---
| 1.2.2.2 | P13 | 代码清单1-3下第2段第2行 | http://helloflask.com/hello/Grey | http://helloflask.com/greet/Grey | 笔误 |
| 1.7 | P23 | 第2个代码块下第1行 | `url_for('say_hello', name='Jack')` | `url_for('greet', name='Jack')` | 笔误 |
| 2.2.1 | P31 | 表2-3左侧下面的两行 | | POST对应的说明列原文为“传输数据”，修改为“创建或更新资源”；PUT对应的说明列原文为“传输文件”，修改为“创建或替换资源” | 改进 | 18.11.18 |
| 2.2.3.3 | P36 | 表2-6后第1个代码块 | `'goback/<int:year>'` | `'/goback/<int:year>'` | 笔误。URL规则漏掉了开头的斜线 | 18.9.28 |
| 2.3.1 | P40 | 第3个代码块 | `{'Location', 'http://www.example.com'}` | `{'Location': 'http://www.example.com'}` | 笔误。返回值中字典里的符号出错 |
| 2.3.2 | P44 | HTML小节的最后1行 | HTTP | HTML | 笔误 |
| 2.3.2.4 | P46 | 倒数第3个代码块 | `return jsonify({name: 'Grey Li', gender: 'male'})` | `return jsonify({'name': 'Grey Li', 'gender': 'male'})` | 笔误。字典中的键未加引号 | 18.10.18 |
| 2.2.3 | P48 | 图2-11 |  | 图中的响应状态码应该为 302 Found | 文图不对应 | 18.10.18 |
| 2.3.4.2 | P50 | 代码清单2-5下第1段第3行 | logged-in cookie| logged_in cookie | 排版错误 | 18.11.8 |
| 2.3.4.2 | P51 | 图2-12后第1个代码块 | | 第9行及以下均应向左缩进4个空格 | 排版错误 | 18.10.18 |
| 2.3.4.2 | P52 | 图2-13后第1段第2行 | logged-in | logged_in | 排版错误 | 18.11.8 |
| 2.3.4.2 | P52 | 代码清单2-6下第2段第2行  | logged-in | logged_in | 排版错误 | 18.11.8 |
| 2.5.4.1.(2) | P67 | “攻击示例”小节第3段文字第2行 | 设为 “';drop table users; --” | 设为 “';drop table students; --” | 笔误 |18.11.2 |
| 4.2.3 | P110 | 代码清单4-2最后1行 | `'login.html'` | `'basic.html'` | 笔误 | 18.9.28 |
| 4.3.1 | P112 | 第1个代码块后第1行 | 3000 | 2000 | 笔误，不同的浏览器对于URL有不同的长度限制，此处的长度为“最佳实践” |
| 4.3.1 | P113 | 代码清单4-5第1行 | `'/'` | `'/basic'` | 笔误 | 18.10.18 |
| 4.4.4.3.(3)第6个代码块下正文第2行 | P127第2个代码块下正文第2行 | | 这个uploads视图 | 这个get_file视图 | 笔误 | 18.10.27 |
| 4.4.4.4 | P128 | 代码清单4-16 | | “检查文件类型”注释下第一行多余缩进4格 | 笔误 | 18.10.18 |
| 5.3.3 | P146 | 第2个代码块 | | 开头可添加一行导入`from app import Note` | 更完善 | 18.10.18 |
| 5.4.1.1 | P147 | ”Create“小节第1个代码块第4行 | `'DON'T BELIEVE……'` | `'DON\'T BELIEVE……'` | 代码错误，字符串漏掉了转义符号 |
| 5.4.1.2 | P150 | 表5-7下的第1个代码块 | `Note.body='SHAVE'` | `Note.body == 'SHAVE'` | 代码错误，少了1个等于号 | 18.9.22 |
| 5.5.2.3 | P160 | ”建立关系“小节第1个代码块 | | 第2行插入`ham.author_id = 1` | 省略步骤，可加可不加 | 18.9.22 |
| 5.5.2.4 | P162 | 代码清单5-11第8行 | `title = ` | `name = ` | 笔误 | 18.9.26 |
| 5.5.2.4 | P163 | ”建立双向关系“小节第3个代码块第6行 | `it.writer = writer` | `it.writer = king` | 笔误 | 18.9.26 |
| 5.5.3 | P164 | 代码清单5-13上面 | 都定义在“多”这一侧，即City类中 | 都定义在“多”这一侧，即Citizen类中 | 笔误 |
| 5.5.4 | P165 | 代码清单5-14后面的代码块第6行 | - | 第6行`>>> china.capital = beijing`移动到第3行 | 笔误 |
| 5.5.4 | P165 | 代码清单5-14后面的代码块第8行 | `<Capital 1>` | `<Capital u'Beijing'>` | 笔误 |
| 5.5.4 | P166 | 代码清单5-14后面的代码块第10行，166页第2行 | `u'China'` | `<Country u'China'>` | 笔误 |
| 5.5.4 | P166 | 代码清单5-14后面的代码块第11行，166页第3行 | `name'Tokyo'` | `name='Tokyo'` | 笔误 | 18.9.26 |
| 5.7.1.2 | P174 | ”delete-orphan“小节上面第1个代码块第1行 | `Post.quer2y.get(2)` | `Post.query.get(2)` | 审校错误。 |
| 5.7.2 | P176 | 代码清单5-18下第1行 | targe | target | 笔误 | 18.9.28 |
| 5.7.2 | P177 | 最后1个代码块上面 | 参数name | 参数named | 笔误 | 18.9.28 |
| 5.7.2 | P177 | 最后1段提示文字 | 监听函数时， | 监听函数。这时 | 审校错误，编辑在捣乱 | 18.9.28 |
| 5.7.2 | - | 全章节多处 | listen_for | listens_for | 笔误 | 18.9.28 |
| 6.1.1 | P181 | 代码清单6-1 | | 第9-13行末尾漏掉分割参数的逗号 | 笔误 | 18.10.27 |
| 7.3.2 | P208 | 第1个代码块第6行 | `render_form(form),action=request.full_path` | `render_form(form, action=request.full_path)` | 审校错误，右侧关闭括号位置出错 |
| 7.3.2 | P208 | 表7-2上面段落的最后一句话 | quick_form() | render_form() | 笔误。历史遗留问题 | 18.9.28 |
| 7.4.3 | P211 | 表7-4下面的提示段落 | https://momentjs.com/docs/displaying/format/ | https://momentjs.com/docs/#/displaying/format/ | 链接变化 | 18.11.5 | 
| 8.1.3 | P229、P231 | 代码清单8-2、8-4 | | 单个蓝本变量名称均应为foo_bp形式，比如admin应为admin_bp | 笔误 | 18.9.24 |
| 8.2.1.1.(4) | P235 | 代码清单8-7后面第1个代码块第3行 | `db.relationship('Comment', backref='post', cascade='all')` | `db.relationship('Comment', back_populates='post', cascade='all, delete-orphan')` | 笔误 |
| 8.2.3 | P247 | 代码清单8-19第2行 | `from wtforms` | `from wtforms.validators` | 笔误 | 18.10.27 | 
| 8.3.1 | P252 | 第1个代码块最后1行 | `'index.html'` | `'blog/index.html'` | 笔误 | 18.10.06 |
| 8.3.1 | P252 | 代码清单8-24文件路径 | templates/index.html | templates/blog/index.html | 笔误 | 18.10.06 |
| 8.3.5 | P263 | 第1个代码块第6行 | `Comment.query.with_parent(post)` | `Comment.query.with_parent(post).filter_by(reviewed=True)` | 笔误 | 18.9.26 |
| 8.3.7 | P267 | 代清清单8-31第4行 | `comment.photo_id` | `comment.post_id` | 笔误 | 18.9.26 |
| 8.3.7 | P267 | 代清清单8-31下方正文第2段最后一行的URL中 | photo | post | 笔误 | 18.9.26 |
| 8.4.1 | P272 | 第1个代码块最后1行 | `>>> False` | `>>> True` | 笔误 | 18.10.27 |
| 8.5 | P275 | “8.5”小节下第2个代码块第2行 | `LoginManger(app)` | `LoginManger()` | 代码错误 | 18.10.27 | 
| 8.6 | P282 | 代清清单8-38第4行 | `'400.html'` | `'errors/400.html'` | 笔误 | 18.10.27 |
| 8.7.1 |P285 | 代码清单8-40下的正文第1行 | manage_category.html | manage_post.html | 笔误 | 18.10.27 | 
| 9.3.3 | P315 | 代码清单9-8下的正文第2段第2行（纸书该页最后1行） | `auth.resend_confirmation` | `auth.resend_confirm_email` | 笔误 | 18.11.5 |
| 9.5.3 | P334 | 代码清单9-19后面的代码块倒数第二行 | `photo.save()` | `db.session.add(photo) 换行 db.session.commit()` | 遗留代码未更新 | 18.10.27 |
| 10.3.6.3 | P468 | ”处理错误响应“小节第1行 | app.error_handler | app.errorhandler | 笔误 |
| 11.4.3.5 | P503 | 代码清单11-11中多处 | `get['XXX']` | `get('XXX')` | 审校错误 |
| 11.5.1 | P509 | 代码清单11-13第5行 | `position === 0&& socket.nsp` | `position === 0 && socket.nsp` | 审校错误。空格缺失 |
| 11.5.3 | P513~P514 | 513页7处，514页8处 |  | 所有的 Pyments 改为 Pygments，pyments 改为 pygments | 笔误 | 18.11.18 |
| 15.7.3 | P625 | 最后1个代码块的第2行 | `git push origm` | `git push origin` | 审校错误。另外，这一行下面的Github应为GitHub |



#### 不重要勘误

此处的勘误多为单词拼写错误或不影响理解和程序运行的笔误，可以忽略。

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
| 1.2.2 | P13| 标题1上面的附注段落 | Lacator | Locator | 拼写错误 | 18.10.25 |
| 1.3.1 | P14 | 标题 | Run，Flask，Run！ | Run, Flask, Run! | 标点错误 |
| 1.3.1 | P14 | ”Run，Flask，Run“小节第1个代码块最后1行 | | 出现多余的缩进 | 排版错误 |
| 1.3.1.3 | P17 | 配置步骤4 | 下列选项 | 下拉选项 | 笔误 |
| 1.3.3 | P18 | ”1.3.3“小节第1行 | Enviroment  | Environment | 拼写错误 |
| 2.2.3 | P34 | 图2-5 |  | 地址栏的地址应为/nothing，和描述对应。图中的/foo在后面实际被定义了 | 笔误 | 18.9.28 |
| 2.3.3 | P47 | 表2-10后面的第1个附注段落 | Respone | Response | 笔误。拼写错误 |
| 2.3.4 | P50~P52 | 代码清单2-5下第1段第3行；图2-13后第1段第2行；代码清单2-6下第2段第2行 | logged-in | logged_in | 笔误 | 18.11.18 |
| 2.5.4.1.(2) | P67 | 纸书该页第1个代码块，电子书“攻击示例”小节第2个代码块 |  | 最后的单引号和前面的分号对调位置 | 笔误 |18.11.5 |
| 2.5.4.1.(2) | P67 | 纸书该页第2个代码块，电子书“攻击示例”小节第3个代码块 |  | 在最后的分号前添加一个半角单引号 | 笔误 |18.11.5 |
| 2.5.4.1.(3) | P67 | ”主要防范方法“小节第1个代码块 | `db.execute('SELECT * FROM students WHERE password=?, password)` | `db.execute('SELECT * FROM students WHERE password=?', password)` | 笔误。字符串漏写右侧关闭引号 |
| 2.5.4 | P69 | 纸书该页最后1行的代码块最后几个字符 | `sript` | `script` | 笔误 | 18.11.5 | 
| 3.1 | P77 | 代码清单3-1下的提示 | HTML5 | HTML | 多余文本。另外，后面的链接需要更新为 https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure |
| 3.3.2 | P89 | 第1个代码块上面的文字第2行 | `_macors.html` | `_macros.html` | 笔误 |
| 3.3.2 | P89 | 第1个注意段落最后1行 | 显示 | 显式 | 笔误 | 18.10.18 |
| 3.4.1 | P93 | 第1~4个代码块 | | 忽略了 Jinja 本身的代码逻辑，读者可忽略 Jinja 语句含义，具体见后面 | 逻辑错误。 | 18.11.5 |
| 3.4.2 | P97 | 注意段落下面正文第2行 | CND | CDN | 笔误 | 18.10.27 |
| 3.4.4 | P101 | 图3-5 | | 地址栏的地址应为/nothing，和描述对应。 | 笔误 | 18.10.1 |
| 4.1 | P105 | 最后一行 | ， | 。 | 笔误 | 18.11.11 |
| 4.2.1 | P108 | 表4-3下面的注意段落 | `内置的验证器通过……` | `内置的验证器使用……` | 改善措辞 | 18.11.5 |
| 4.2.3 | P110 | 代码清单4-3第3行 | `{{ from.username.label }}{{ form.username }}<br>` | `{{ from.username.label }}<br>{{ form.username }}<br>` | 改进 | 18.11.5 |
| 4.2.3 | P110 | 代码清单4-3第4行 | `{{ from.password.label }}{{ form.password }}<br>` | `{{ from.username.label }}<br>{{ form.username }}<br>` | 改进 | 18.11.5 |
| 4.3.3 | P117 | 代码清单4-7第4行 | `form.username()` | `form.username` | 笔误。此处的括号可有可无，去掉以保持风格上的统一 | 18.9.24 |
| 4.4.4.1 | P123 | 代码清单4-13第1行 | `flask wtf` | `flask_wtf` | 审校错误 | 18.9.24 |
| 4.4.4.4 | P128 | 代码清单4-16上面的第1个代码块第3行 | | 缺少右侧关闭括号 | 笔误 | 18.10.18 |
| 4.4.5 | P131 | 代码清单4-19下正文段落第3行 | `Ture` | `True` | 笔误 | 18.11.5 |
| 5.3.1 | P143 | 表5-2最后1行 | SQlite | SQLite | 大小写错误 | 18.10.27 |
| 5.5.2 | P159 | 表5-4下的注意段落第2行 | Flask-SQLlchemy | Flask-SQLAlchemy | 笔误 | 18.10.27 |
| 5.8 | P177 | 最后1行 | 本章要介绍的 | 本章介绍的 | 笔误 | 18.9.28 |
| 6.1.3 | P183 | 代码清单6-3第9行 | `return redirect(url_for('idnex'))` | `return redirect(url_for('index'))` | 笔误 | 18.10.27 |
| 6.2 | P183 | 6.2及6.2.1章节标题以及目录共**4处** | SendGird | SendGrid | 笔误 | 18.10.27 |
| 7.2.3.1 | P202 | 代码清单7-3的文件路径 | sayhello.py | models.py | 笔误 |
| 7.3.1 | P207 | 3.7.1节中最后一段话中的bootstrap_load_js() | bootstrap_load_js() | bootstrap.load_js() | 笔误 | 18.11.17 |
| 7.5 | P213 | 最后一行代码 | fake = Faker('zh_CN'))|  fake = Faker('zh_CN') | 笔误 | 18.11.17 |
| 8.1 | P220 | 文件目录树 | | 目录树漏掉了 __init__.py 文件 | 笔误。 | 18.10.1 |
| 8.1.3 | P229 | 第2个提示段落 | 新创建的模块 | 新创建一个模块 | 审校错误。 | 18.9.24 |
| 8.2.1.3 | P237 | 代码清单8-9第10行 | | 缩进少一格 | 排版错误 | 18.10.18 |
| 8.3.3 | P261 | 代码清单8-27 | | `<div class="modal-body">` 所在的行以及下面2行均向右缩进8格 | 排版错误 | 18.11.5 |
| 8.3.5 | P264 | 代码清单8-29第12行 | `(%Y-%m-%dT%H:%M:%SZ')` | `('%Y-%m-%dT%H:%M:%SZ')` | 笔误，漏掉左侧引号 | 18.10.27 |
| 8.7.2.1 | P293 | 图8-16上面的提示段落 | HTmL | HTML | 审校错误，大小写错误 |
| 9.10.1 | P379 | 代码清单9-59下面的代码块 | | 第2行向右缩进1格，第3行向左缩进，和第2行对齐。 | 排版错误 | 18.11.18 |
| 9.13 | - | 9.13小节最后代码清单上面的文字 | innit_app() | init_app() | 笔误 | 18.11.04 |
| 10.2.5 | P438 | 标题上面的附注文字 | 生成帮助信息 | 生成的帮助信息 | 审校错误。编辑以为自己在改病句，实际上却是在制造病句 |
| 10.3.1.4 | P443 | “10.3.2”小节上面段落倒数第3行 | RSET | REST | 笔误 |
| 10.3.3.5 | P453 | 代码清单10-13下面的提示段落最后1行 | flask-restless | Flask-Restless | 大小写错误 |
| 12.3.2 | P527 | 代码清单12-2第7行 | test_app_exsit | test_app_exist | 拼写错误 |
| 14.4.2 | P574 | 第2个提示段落上面两处 | python(3) | python3 | 审校错误 |

关于URL长度限制的详情可以参考[WWW FAQs: What is the maximum length of a URL?](https://www.boutell.com/newfaq/misc/urllength.html)。


### 断行连接符错误

编辑人员在处理书稿时，对断行单词添加了连字符，但对于编程变量并不需要这样处理，容易导致误解。我过了一遍全书，找出了这些错误的位置
共42处。你可以选择不修改，了解即可，如果非要修改，请沿着页面最右侧边缘进行定位。因为电子书页数不固定，目前无法确定，请等待重印更新。

* P106下面Password-
* P320第7行，看页面最右侧，back_popu- 去掉后面的连字符。
* P329第3行，user- 去掉后面的连字符
* P338代码清单9-21倒数第4行 user-
* P339倒数第2行 file-
* P342上面的代码块两处 share- 和 times-
* P344下面的代码块1处，倒数第8行，dis-。
* P346第一个代码块下面第1行 connec-
* P347下面的代码块 de-
* P354倒数第2个代码块com-
* P356附注段落 getboot-
* P369下面代码块 pagina-
* P370第1行pagina-
* P376页面中部 follo-
* P377页面上部 error-
* P383 页面中部notifica-
* P389页面上方up-
* P393页面上方正文 old_pass-
* P394下方三处 notifica-，倒数第二行还有一个noti-fication需要去掉中间的连字符
* P396第一行colle-
* P398 中部regi-
* P404下面user-
* P419上面style-
* P440中部，两处for-和date-
* P442底部disserta-
* P459上部BadSigna-
* P460下部sec-
* P461中部sty-
* P472上面Authori-
* P487中部_annony-mous_去掉中间的连字符
* P517上部notifica-
* P539下部Phantom-
* P556下部Cach-（只去掉最后的连字符）
* P569上部WARN-
* P586上部super-
* P599下部的require-和pip-
* P608下部Py-
* P631下部Doc-
* P671上部Null-
* P678下部templa-
* P679中部Environ-
* P682中部Bit-，同时这一行的Github需要改为GitHub


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
* 第1章：Pipenv自2018.6.25版本后在Windows中激活虚拟环境后会显示虚拟环境提示符（具体版本号待确认）。
* 第15章中的Flask-Share源码对应0.1.0版本。
