
## 临时勘误

为重印新版本暂存的勘误，未来或许会合并到 errata.md 里。

### 1-2（第 1 版第 2 次印刷）

发布时间：2019/1/1

位置 | 错误 | 正确 | 备注/时间 |
--- | --- | --- | ---
| 2.2 P30 请求报文示例表格 | | URL /hello 改为 http://helloflask.com/hello?name=Grey | 19.2.2 |
| 2.2 P30 请求报文示例表格 | | 去掉主体一栏的内容 | 19.2.2 |
| 2.2 P30 请求报文示例表格下方正文 | 如果 URL 中包含查询字符串，或是提交了表单，那么报文主体将会是查询字符串和表单数据。 | 如果提交了表单，那么报文主体将会是表单数据（查询字符串通常会直接通过 URL 传递）。 | 19.2.2 |
| 2.2 P31 命令行输出 | /hello | /hello?name=Grey | 19.2.2 |
| 3.2.4 2.自定义测试器 P86下方| 我们创建了一个没有意义的baz过滤器 | 我们创建了一个没有意义的baz测试器 | 笔误 19.1.9 | 
| 4.3.1 P115 第 2 小节的代码块第 5 行 | `Length(8, 128)` | `Length(6, 128)` | 前后不一致（1-3 重印时需要反过来调整另外 3 处），18.12.28 |
| 5 P139 第 1 个代码块 | | `$ flask run` 上面添加一行 `$ flask initdb  # 初始化数据库，后面会详细介绍` | 疏漏 19.1.5 |
| 5.4.2 P153 代码清单 5-5 | | 删掉第 3 行，最后一行删除括号中的`, form=form` | 代码未更新 18.12.24 |
| 5.4.2 P155 代码清单 5-8 第 3 行 | `DeleteForm()` | `DeleteNoteForm()` | 代码未更新 18.12.24 |
| P164 第 2 段第 2 行和第 3 行两处 | backref() 函数 | db.backref() 函数 | 优化 19.3.7 |
| P164 第一个代码块第 3 行 | `backref=backref(...)` | `backref=db.backref(...)` | 错误 19.3.7 |
| 7.3.1 P207 3.7.1节中最后一段话中 | bootstrap_load_js() | bootstrap.load_js() | 笔误 18.11.17 |
| 7.4.3 P213 最后 1 个附注段落 | bootstrap.bundle.min.css |  bootstrap.bundle.min.js | 笔误 18.12.5 |
| 7.5 P214 该页（节）最后 2 个代码块的最后 1 行 | | 两处均向左缩进 4 格，和上面对齐 | 排版错误 18.12.6 |
| 8.2.1 P237 代码清单 8-8 倒数第 3 行 | | 删除这一行 | 后续内容前置 19.1.13 |
| P263 代码清单 8-29 第 2 行 | `{{ comments\|length }} Comments` | `{{ pagination.total }} Comments <!-- 使用 pagination.total 获取分页条目总数 -->` | 优化 19.3.5 |
| 8.3.5 P264 图 8-8 上的代码块第2行 | `{{ comment.replied.author.name }}` | `{{ comment.replied.author }}` | 笔误 18.12.6 |
| 8.3.7 P268 第1行 | photo | show_post | 笔误 18.12.6 |
| 8.4.1 P273 纸书该页第 2 个代码块，电子书 8.4.2 上面倒数第 2 个代码块。第 5、7 行 | `check_password` | `validate_password` | 笔误 18.12.6 |
| 8.5.3 P278 代码清单8-37代码块第1行 | `from flask_login import logout_user` | `from flask_login import logout_user, login_required` | 代码错误 18.12.6 | 
| 8.7.1.2 P288 代码清单8-42代码块倒数第2行  | `.show_post` | `blog.show_post`  | 笔误 18.12.6 | 
| 8.7.1.3 P290 第1个代码块倒数第5行  | `.show_post` | `blog.show_post`  | 笔误 18.12.6 |
| 8.7.2 P292 代码清单8-44代码块倒数第1行  | `.show_post` | `blog.show_post`  | 笔误 18.12.6 | 
| 9.1.1 P301 该页最后 1 行，电子书该节第 2 个代码块最后一行 | | 向左缩进 4 格 | 排版错误 18.12.6 |
| 9.1.1 P302 9.1.2 标题上面的代码块 | `bluelog` | `myapp` | 笔误 18.12.6 |
| P309 代码清单 9-2 倒数第 6 行 | field.data | field.data.lower() | 优化 19.3.5 |
| 9.3.2.1 P312 第二个代码块上正文倒数第1行 | Operations字典中 | Operations类中| 笔误 18.12.10 |
| 9.3.2.2 P314 代码清单9-6代码块最后1行 | `url_for('.reset_confirmation')` | `url_for('.reset_confirm_email')`| 笔误 18.12.12 |
| 9.4.4 P324 代码清单9-14代码块第4-5行 || 两处均向左缩进 4 格 | 排版错误  18.12.10 |
| P332 图 9-4 下面第 2 行 | dropzone_upload 视图 | upload 视图 | 错误 19.3.5 |
| 9.5.3 P334 9.6 小节上面的代码块最后一行模板字符串 | `home/upload.html` | `main/upload.html` | 遗留代码未更新 18.12.17 |
| 9.5.3 P334 9.6 小节上面的代码块 | | 代码中的 400 和 800 分别替换为配置变量 `current_app.config['ALBUMY_PHOTO_SIZE']['small']` 和 `current_app.config['ALBUMY_PHOTO_SIZE']['medium']` | 遗留代码 18.12.17 |
| P360 代码清单 9-41 倒数第 2 行和倒数第 8 行**两处** |  `self.collected`  | `Collect.query.with_parent(self)` | 错误 19.3.5 |
| P363 代码清单9-45 倒数第 6 行 | collections | collects | 错误 19.3.5 |
| P363 代码清单9-45 第 3 行 | `... import user_card with context %}` | `... import user_card %}` | 提前 19.3.5 |
| P367 正文第 3 行 | if_following() | is_following() | 错误 19.3.5 |
| P368 第 2 段第 2 行 | | 去掉“和 is_followed_by()” | 多余内容 19.3.5 |
| 9.8.3 P363 代码清单9-45代码块倒数第6行 | `{% if collections %}` |`{% if collects %}`| 笔误 18.12.10 |
| 9.9.4 P371 代码清单9-53的路径 | albumy/templates/profile_popup.html | albumy/templates/main/profile_popup.html | 笔误 18.12.21 |
| 9.9.4 P375 代码清单 9-56 下面的代码块第二行 | id="followers-count" | id="followers-count-{{ user.id }}" | 笔误 18.12.21 |
| 9.11.2 P388 最后一行 | 渲染avatar.html模板 |渲染change_avatar.html模板| 笔误 18.12.10 |
| 9.11.2 P389 第一个代码块下正文第1行 | avatar.html模板继承自settings.html模板 |change_avatar.html模板继承自settings/base.html模板| 笔误 18.12.10 |
| 9.11.2 P389 代码清单9-71代码块第1行 | `{% extends 'user/settings.html' %}` |`{% extends 'user/settings/base.html' %}`| 笔误 18.12.10 |
| 9.11.6 P397 代码清单9-79代码块倒数第5行 | `current_user` |`current_user._get_current_object()`| 笔误 18.12.10 |
| 9.11 P385 代码清单9-66倒数第9行 | `{{ render_nav_item('user.notification_setting', 'Notification and Privacy') }}` | `{{ render_nav_item('user.notification_setting', 'Notification') }} {{ render_nav_item('user.privacy_setting', 'Privacy') }}` | 代码与实际项目不符 18.12.24 |
| 9.11.2 P389 代码清单9-71倒数第4行 | `{{ render_form(crop_form) }}` | `{{ render_form(crop_form, action=url_for('.crop_avatar')) }}` | 笔误 18.12.24 |
| P395 第 1 个代码块第 3 行 | show_collections | public_collections | 错误 19.3.5 |
| P396 提示段落 | show_collections | public_collections | 错误 19.3.5 |
| P406 代码清单 9-85 第 3 行 | | 在这一行最后紧跟着括号添加（注意不要漏掉开始的英文句点） `.strip()` | 优化，避免输入空格作为搜索词 19.3.5 |
| P412 代码清单 9-90 倒数第 3 行 | field.data | field.data.lower() | 优化 19.3.5 |
| P417 文件目录树倒数第 6 行 | app.py | todo.py | 错误 19.3.5 |
| 10.1.1 P420 第 2 小节第一个代码块第 7 行 | `{{ url_for('todo.clear_item') }};` | `{{ url_for('todo.clear_items') }};` | 笔误 18.12.27 |
| 10.1.4 P425 第一个代码块第 6 行 | `jsonify(message='Invalid item body.'), 400` | `return jsonify(message='Invalid item body.'), 400` | 笔误 19.1.20 |
| 10.3.3 P447 第 1 小节/该页最后一个代码块 | `... import api` | `... import api_v1` | 笔误 18.12.28 |
| 10.3.3 P447 第 1 小节/该页最后一个代码块 | `csrf.exempt(api)` | `csrf.exempt(api_v1)` | 笔误 18.12.28 |
| 10.3.3 P453 代码清单10-13第一行中的methods参数 | `methods=['GET', 'POST']` | `methods=['GET']` | 与原定的方法不一致 18.12.28 |
| 10.3.3 P453 代码清单10-13第二行中的第一个参数 | `'/token'` | `'/oauth/token'` | 与实际项目不一致 18.12.28 |
| 10.3.3 P453 代码清单10-13第二行中的methods参数 | `methods=['GET']` | `methods=['POST']` | 与实际项目不一致 18.12.28 |
| 10.3.5 P462 代码清单10-20倒数第4行 | `item.author,` | `item.author.username,` | 笔误 18.12.28 |
| 11.3.2 P483 代码清单11-4倒数第2行 | | 花括号"}"后添加一个逗号"," | 笔误 18.12.28 |
| 11.3.2 P484 代码清单11-5第2行 | `$('message')` | `$('.messages')` | 笔误 18.12.28 |
| 11.4.1 P491 该节最后一段正文的第1行 | views包 | blueprints包 | 笔误 18.12.29 |
| 11.4.3 P498 附注段落下方正文第2行 | provide_name | provider_name | 笔误 18.12.29 |
| 11.4.3.5 P503 最后一个代码块 | `access_token = resp.get('access_token')` | `access_token = response.get('access_token')` | 笔误 18.12.29 |
| 11.4.3.6 P505 提示段落上方的代码块 | `@oauth_bp.route(...)` | `@auth_bp.route(...)` | 笔误 18.12.29 |
| 11.4.4 P506 第二个代码块 |  | 所有 resp 改为 response | 笔误 18.12.29 |
| 11.4.4 P506 第二个代码块 | | 增加if response is not None:... else:...语句，具体参考源码 | 笔误 18.12.29 |
| 11.5.1 P508 代码清单11-12 | `'_messages.html'` | `'chat/_messages.html'` | 笔误 18.12.29 |
| 11.5.1 P509 代码清单11-13第5行 | `position === 0&& socket.nsp! == '/anonymous'` | `position === 0 && socket.nsp !== '/anonymous'` | 审校错误，空格错误 18.12.29 |
| 11.5.1 P510 代码清单11-13倒数第6行 | `toast('No more messages.');` | `alert('No more messages.');` | 此项目中未定义toast函数 18.12.29 |
| 11.5.4 P516 代码清单11-15第3行 | `'message'` | `'new message'` | 笔误 18.12.29 |
| 11.5.4 P516 代码清单11-15第6行 | `document.title = '(' + message_count + ') ' + document.title;` | `document.title = '(' + message_count + ') ' + 'CatChat';` | 消息数量会随着事件多次发生而不断追加在原标题前 18.12.29 |
| 11.5.5 P517 代码清单11-17第6行 | `data.name` | `data.nickname` | 笔误 18.12.30 |
| 11.5.5 P517 代码清单11-17第7行 | `icon: ...` | `icon: data.gravatar` | 笔误 18.12.30 |
| 11.5.5 P518 最后1个代码块第5行 | `'_message.html'` | `'chat/_message.html'` | 笔误 18.12.30 |
| 11.5.5 P518 最后1个代码块第6行字典的值 | `message_body` | `html_message` | 笔误 18.12.30 |
| 12.3.1 P526 代码清单12-1 | | setUp方法最后面追加一行代码`self.client = app.test_client()` | 代码缺失 19.01.05 |
| 12.3.2 P527 提示段落下方的正文第3行 | assertEqual() | assertTrue() | 笔误 19.01.05 |
| 12.3.2 P527 代码清单12-3 test_404_page方法的注释 | # 测试 400 错误页面 | # 测试 404 错误页面 | 笔误 19.01.05 |
| 12.3.3 P534 代码清单12-6最后1个导入语句 | `from bluelog.models import User` | `from bluelog.models import Admin` | 笔误 19.01.06 |
| 13.1.2 P550 代码清单13-1 | `@app.after_app_request` | `@app.after_request` | 笔误 19.01.06 |
| 13.1.2 P550 代码清单13-1 | | 两处current_app改为app | 笔误 19.01.06 |
| 13.3 P557 命令行命令 | `$ cd cache` | `$ cd assets` | 笔误 19.01.06 |
| 14.3.1 P567 第二个代码块第2行| `token_urlsafe(16)` |  `secrets.token_urlsafe(16)` | 笔误 18.11.28 |
| 14.3.4 P569 代码清单14-1 register_logger函数缺少app参数| `register_logging()` |  `register_logging(app)` | 笔误 18.11.28 |
| 14.4.7 P584 倒数第2个代码块上方段落第5行| 放在/etc/supervisord.conf路径下 | 放在/etc/supervisor/conf.d路径下 | 笔误 18.11.28 |
| 14.3.4.1 P569 代码清单14-1上方正文 | `register_logger()` | `register_logging()` | 与实际源码不符 19.01.21 |
| 14.3.4.1 P569 代码清单14-1 | `register_logger()` | `register_logging(app)` | 与实际源码不符 19.01.21 |
| 14.3.4.1 P569 代码清单14-1 | RotatingFileHandler的第一个参数 | `os.path.join(basedir, 'logs/bluelog.log')` | 与实际源码不符 19.01.21 |
| 14.3.4.2 P570 代码块 | `register_logger()` | `register_logging(app)` | 与实际源码不符 19.01.21 |
| 14.3.4.3 P571 代码清单14-2 | `register_logger()` | `register_logging(app)` | 与实际源码不符 19.01.21 |
| 14.3.4.3 P571 代码清单14-3 | `register_logger()` | `register_logging(app)` | 与实际源码不符 19.01.21 |
| 14.3.4.3 P571 代码清单14-3 | 5处`os.getenv()` | `app.config[]` | 与实际源码不符 19.01.21 |
| 14.4.3.1 P576 提示段落第二行 | C/Users/Administrator/.ssh | C:\Users\Administrator\.ssh | 错误 19.01.21 |
| 15.5 P611 正文第5行 | 在模板中提供load()方法资源。 | 在模板中提供load()方法加载静态资源。 | 句子不完整 19.01.21 |
| 15.5.1 P612 页面中部代码块 | `def load(css_url=None, js_url=None):` | `def load(css_url=None, js_url=None, serve_local=False):` | 与实际源码不符 19.01.21 |
| 15.5.1 P612 页面中部代码块 | `if current_app.config['SHARE_SERVE_LOCAL']:` | `if serve_local or current_app.config['SHARE_SERVE_LOCAL']` | 与实际源码不符 19.01.21 |
| 15.5.1 P612 页面中部代码块最后1行中的filename参数 | `filename='js/share.min.js'` | `filename='js/social-share.min.js'` | 笔误 19.01.21 |
| 15.6.1 P614 代码清单15-8中Share类的init_app方法中的blueprint | Blueprint缺少static_folder和static_url_path参数 | 见代码清单15-5或项目源码 | 笔误 19.01.21 |
| 15.6.1 P614 代码清单15-8中Share类的init_app方法 | 没有将扩展添加到模板上下文 | 添加代码`app.jinja_env.globals['share'] = self` | 代码缺少 19.01.21 |
| 15.6.1 P614 代码清单15-8中Share类的init_app方法最后1行第2个参数 | True | False | 与实际源码不符 19.01.21 |
| 15.6.1 P615 代码清单15-7和代码清单15-8中Share类的create方法参数 | `addition_class=None` | `addition_class=''` | 与实际项目不符 19.01.21 |
| 16.2.4 P639 最后1个段落的第2行 | 在不基于线程、greenlet或单进程实现的并发服务器上 | 在不基于线程、Greenlet 或进程实现并发的服务器上 | 笔误 18.12.31 |
| 16.4.2 P649 最后1行| Flask.route()是Flask类的类方法 | Flask.route()是Flask类的实例方法 | 笔误 19.1.1 |
| 16.4.3 2. 堆栈与LocalStack  P659 第1段第3行| 并将数据的字典名称设为'stack'。| 并将储存上下文对象的列表名称设为'stack' | 笔误 19.1.4 |
| 16.4.5 P672 第一段第一行 | 对传入的**请求对象**调用 | 对传入的**响应对象**调用 | 笔误 19.2.8 |


**P412** 添加 validate_username() 方法定义（同时添加到 1-1 勘误）：

```python
def validate_username(self, field):
    if field.data != self.user.username and User.query.filter_by(username=field.data).first():
        raise ValidationError('The username is already in use.')
```

**P363** 正文第 1 段，原文：

我们在第 3 章曾经介绍过 Jinja2 的上下文机制，因为 user_card 宏里使用了 Flask-Login 提供的 current_user 变量，所以我们需要在导入时使用 with context 指令显式声明包含上下文：

改为：

根据第 3 章介绍的 Jinja2 上下文机制，因为 user_card 宏后面会使用 Flask-Login 提供的 current_user 变量，到时你需要为相关的导入语句追加 with context 指令显式声明包含上下文：


**P393** 代码清单9-74 从该页第 3 行到第 8 行，原文为：

```python
    if form.validate_on_submit() and current_user.validate_password(form.old_password.data):
        current_user.set_password(form.password.data)  # 重设密码
        db.session.commit()
        flash('Password updated.', 'success')
        return redirect(url_for('.index', username=current_user.username))
```
修改为：

```python
    if form.validate_on_submit():  # 验证表单是否通过验证
        if current_user.validate_password(form.old_password.data):  # 验证旧密码
            current_user.set_password(form.password.data)  # 设置新密码
            db.session.commit()  # 提交数据库会话
            flash('Password updated.', 'success')
            return redirect(url_for('.index', username=current_user.username))
        else:
            flash('Old password is incorrect.', 'warning')  # 旧密码不对则显示提示
```

**P409** 代码清单 9-88 在第 2 行和第 10 行（@permission 开头的两行）上面分别插入新的一行，内容为 `@login_required`，比如：

```python
@admin_bp.route('/lock/user/<int:user_id>', methods=['POST'])
@login_required
@permission_required('MODERATE')
```

**P275** 8.5 小节标题上面添加提示段落：

提示 在 fakes.py 脚本里的 fake_admin() 函数中，我们需要在 admin 对象创建后，为虚拟用户记录设置密码：admin.set_password('helloflask')。


#### 不重要

位置 | 错误 | 正确 | 备注/时间 |
--- | --- | --- | ---
| 2.2.2 P33 正文第一行 | MutliDict | MultiDict | 笔误 18.12.24 |
| 2.3.1 P41 代码清单 2-2 第 7 行 | redierct | redirect | 笔误 18.12.24 |
| 2.3.2.4 P45 JSON代码示例 | "heading":"Remider", |  "heading":"Reminder",  | 笔误。单词拼写错误。 18.11.28 |
| 2.2.2 P33 图 2-4 上面一行 | requset | request | 笔误 18.12.28 |
| 2.2.2 P33 代码清单 2-1 最后一行 | `'<h1>Hello, %s!<h1>'` | `'<h1>Hello, %s!</h1>'` | `<h1>` 关闭斜线 18.12.28 |
| 2.2.2 P33 代码清单 2-1 最后一行 | | 该行注释缩进出错，向左移动至保留 2 个空格 | 排版错误 18.12.28 |
| 3.2.5 P87 正文共 5 处 | enviroment | enviro**n**ment | 拼写错误 18.12.28 |
| 3.1.1 P76 代码清单 3-1 文件路径 | template/watchlist.html | template**s**/watchlist.html | 笔误 18.12.28 |
| P89 最后一个代码块上面的段落 | 使用第一个列表 | 使用**前**一个列表 | 优化 19.3.5 |
| P149 表 5-6 左边一列第 1 行和第 5 行两处 | ident | id | 优化 19.3.5 |
| P150 表 5-7 左边一列的标题 | 查询过滤器名称 | 过滤方法 | 优化 19.3.5 |
| P237 代码清单 8-10 第 2 行 | | 空白行写入内容 `import random` | 优化 19.3.5 |
| 3.4.2 P97 注意段落最后一行 | Boostrap | Boo**t**strap | 笔误 18.12.28 |
| 3.4.4 P101 图 3-5 下面第 1 行文字 | 处理器和模块 | 处理器和模**板** | 笔误 19.1.13 |
| 4.4.4.1 P123 代码清单4-13第3行 | | 字符间距过大。 | 排版错误 19.1.5 |
| 4.4.5.2 提示段落 | https://flask-ckeditor.readthedocs.io/configuration.html | https://flask-ckeditor.readthedocs.io/en/latest/configuration.html | 笔误 19.1.5 |
| 5.5.2 P160 正文最后一行、P161 第一行 | Aritcle | Article | 笔误 18.12.24 |
| 7.2 P202 代码清单 7-3、7-4、7-7 | 补全路径，相应加入 sayhello/ 和 templates/ | 19.2.2 |
| 7.2.3 P204 代码清单7-5后面的代码块第4行 | | `messages = Message.query.order_by...`向后缩进1格 | 缩进 19.01.11 |
| 7.5 P213 最后一行代码 | `fake = Faker('zh_CN'))` |  `fake = Faker('zh_CN')` | 笔误 18.11.17 |
| 8.2.1 P239 代码清单 8-12 文件路径 | bluelog/commands.py | bluelog/__init__.py | 遗留代码未更新 19.1.13 |
| 8.2.1 P240 8.2.2 标题上面的代码块 | | 三个点那一行应该向左缩进 4 格，和上面的美元符号对齐 | 排版错误 19.1.13 |
| 8.3.5 P265 第1个代码块倒数第11行 | `Reply</a>` | `Reply</a></div>` | 笔误 18.12.6 |
| 8.7.2.2 P294 代码清单8-45代码块下正文第1行  | `Ture` | `True`  | 笔误 18.12.6 | 、
| 8.5 P276 提示上方段落第一行 | UserMinxin | UserMixin | 笔误 18.12.23 |
| 8.5.3 P279 代码清单 8-37 第 4 行 | @login_required | @login_required  # 用于视图保护，后面会详细介绍 | 添加注释 19.1.5 |
| P299 | | Flask-Avatars 版本 升级为 0.2.2 | 更新 19.3.5 |
| 9.2 P304 图9-1左上角多了一个"搜索" | `搜索` | 去掉一个`搜索` | 笔误 18.12.10 |
| 9.2 P310 代码清单9-3代码块第7行 | `url_for ('main.index')` |`url_for('main.index')`| 笔误 18.12.10 |
| P327 最后 1 个代码块上方文字 | 使用**分号**隔开 | 使用**逗号**隔开 | 错误 19.3.5 |
| P330 代码清单 9-17 下面的段落第 2 行 | Photo 模型和 User 模型 | User 模型和 Photo 模型 | 优化 19.3.5 |
| 9.8.2 P360 代码清单9-41代码块上访正文倒数第3行 | 实际动作是有用户做出的| 实际动作是由用户做出的| 笔误 18.12.10 |
| 9.9.1 P365 9.9.1 标题下正文第一行 | Uesr | User | 笔误 18.12.21 |
| 9.9 P365 代码清单9-47下方的正文 | timastamp | timestamp | 笔误 18.12.21 |
| 9.7.1 P340 代码清单 9-24 第 2 处注释 | 主要 | 主页 | 笔误 18.12.17 |
| 9.7.1 P339 代码清单 9-23 路径 | macros.py | macros.html | 19.2.2 |
| 9.7.1 P340 代码清单9-24 上方 | Photo_card() | photo_card() | 19.2.2 |
| 9.7.1 P340 代码清单9-24 导入语句第二行 | form | from | 19.2.2 |
| P364 倒数第 3 行 | collections 模板 | 收藏页面模板 | 优化 19.3.5 |
| 9.11.2 P388 提示下方的正文 | Scripts块 | scripts块 | 笔误 18.12.24 |
| P393 代码清单 9-75 | | 代码清单的文件路径和介绍中间添加缺失的中文引号 | 修正 19.3.5 |
| P406 代码清单9-86 |  | 代码清单文件路径改为“albumy/templates/main/search.html” | 错误 19.3.5 |
| 10.1 P417 项目结构示意图 | | blueprints下的__init__.py多缩进了 4 格 | 排版错误 18.12.27 |
| 10.2.2 P427 倒数第5行 | ISO 639?1 | ISO 639-1 | 笔误 18.12.28 |
| 10.2.4 P434 第 2 小节注意段落上方的正文段落的第一行 | message.po | messages.po | 笔误 18.12.28 |
| 10.2.4 P436 图10-3下方的正文第二行 | message.po | messages.po | 笔误 18.12.28 |
| 10.3.1 P442 倒数第5行 | Simple Object Acsess Protocol | Simple Object Access Protocol | 笔误 18.12.28 |
| 10.3.3 P446-P447 目录结构示意图 | | v1包下的4个模块少缩进一级，且apis子包缺少__init__.py模块 | 排版错误 18.12.28 |
| 10.3.4 P454 第二段正文的第二行 | Isssue | Issue | 笔误 18.12.28 |
| 11.1 P476 目录结构示意图 | | blueprints目录向左缩进一级 | 笔误 18.12.28 |
| 11.4.4 P507 正文第一行 | ture | true | 笔误 18.12.29 |
| 12.3.2.2 P532 正文第4个段落的最后1行 | JOSN | JSON | 笔误 19.01.05 |
| 12.3.2.3 P532 代码清单 12-5 第一个注释 | | 注释上面添加 1 个空行，注释前删除 1 个空格 | 排版错误 19.1.13 |
| 12.3.2.3 P532 代码清单12-5 | `from sayhello.commands import forge` | `from sayhello.commands import forge, initdb` | 导入缺失 19.01.05 |
| 12.3.3 P534 代码清单12-6第2个导入语句 | `from flask import current_app, url_for` | `from flask import url_for` | 多余的导入 19.01.06 |
| 12.3.3 P534 代码清单12-7第2个导入语句 | `from flask import current_app, url_for` | `from flask import url_for` | 多余的导入 19.01.06 |
| 12.3.3 P533 代码清单12-6上方正文最后第2行 | tearDow() | tearDown() | 笔误 19.01.06 |
| 12.4.3 P540 代码清单12-10中test_index方法中self.assertIn()的第1个参数 | 'Todoism makes everything clear.' | 'We are todoist, we use todoism.' | 遗留代码未更新 19.01.06 |
| 12.6 P546 第1个附注段落上方的正文第2行 | 弃用 | 启用 | 笔误 19.01.06 |
| 13.3 P557 第2个提示段落 | CND | CDN | 笔误 19.01.06 |
| 13.3.3 P560 第1段正文第3行 | style块 | styles块 | 笔误 19.01.06 |
| 14.3.4 P569 第一段正文下方的代码 | `app.logger.warning('A wraning message.')` | `app.logger.warning('A warning message.')` | 笔误 19.01.21 |
| 14.3.5 P572 代码块 wsgi.py 定义 | 导入语句补充 `import os` | 19.2.2 |
| P578 第 1 个附注段落 | GitHub的免费账户只能创建公开仓库，为此你可以考虑使用BitBucket（https://bitbucket.org），它提供不限数量的免费私有仓库。 | GitHub（https://github.com） 和 BitBucket（https://bitbucket.org） 均支持免费创建私有仓库，你可以在创建仓库时进行选择。 | 更新 19.3.5 |
| 16.5 P680 附注第2行 | Pocco风格指南 | Pocoo风格指南 | 笔误 19.01.21 |
| 16.4.2.1 P650 最后第2段正文第1行 | view_function | view_functions | 笔误 19.01.21 |
| 16.4.2.2 P653 代码清单16-15中的注释 | 出于 | 处于 | 笔误 19.01.21 |
| 14.4.5 P579 下方正文 | WGSI | WSGI | 笔误 19.01.21 |
| 15.5 P611 正文第3行 | | 多一个句号 | 笔误 19.01.21 |
| 15.5.1 P611 倒数第2段正文第1行 | laod() | load() | 笔误 19.01.21 |
| 15.5.1 P612 代码清单15-5中init_app()方法 | `static_folder='static ,` | `static_folder='static,` | 空格错误 19.01.21 |
| 15.5.1 P612 代码清单15-5中init_app()方法 | | 倒数第2行去除一个多余的)符号 | 符号错误 19.01.21 |
| P630 倒数第 2 行 | “f” | “f（红色背景）” | 优化 19.3.5 |
| 16.4.1.1 P647 正文第1行 | Ture | True | 笔误 19.01.21 |
| 16.4.1.2 P648 代码清单16-8中的注释 | HTPP | HTTP | 笔误 19.01.21 |
| 16.4.3 3.代理与LocalProxy P660 Cython交互代码片段第8第9行| 代码与第6第7行重复，可删除 | 校对错误 | 19.1.7 |
| 16.4.5 P669 代码清单16-28 多行注释| 一个字典，每当产生改变化时会调用传入的参数 | 一个字典，每当产生变化时会调用传入的参数 | 笔误 19.1.9 |


**P7** 附注段落，原文为：

附注 包括Flask在内，Flask的5个依赖包都由 Pocoo 团队（http://www.pocoo.org/）开发，主要作者均为Armin Ronacher（http://lucumr.pocoo.org/），这些项目均隶属于Pallets项目（https://www.palletsprojects.com/）。

修改为：

附注 包括Flask在内，Flask的5个依赖包都由 Pallets 团队（http://www.palletsprojects.com/）开发，主要作者均为 Armin Ronacher（http://lucumr.pocoo.org/），这些项目均隶属于Pallets Projects。


**P181** 代码清单6-1 第 9-13 行（以 MAIL 开头的那 6 行），去掉等号“=”两边的空格。

**P214** 代码清单 7-8 第 2 行修改，并新插入一行： 

原文：

```py
from sayhello import app
...
```

修改为：

```py
from sayhello import app, db
from sayhello.models import Message
...
```

拼写错误，全书多处：Crtl 改为 Ctrl，下面是已知的错误位置：
* P300 注意段落
* P220 注意段落
* P195 第二个注意段落
* P416 注意段落
* P475 注意段落
* P15 正文第 1 行
* P20 提示段落上面
* P21 提示段落中两处
* P577 页面中部两处
* P580 页面中部
* P584 页面中部
* P633 第1行
