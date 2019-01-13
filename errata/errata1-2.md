
## 临时勘误

为重印新版本暂存的勘误，未来或许会合并到 errata.md 里。

### 1-2（第 1 版第 2 次印刷）

发布时间：2019/1/5

位置 | 错误 | 正确 | 备注/时间 |
--- | --- | --- | ---
| 3.2.4 2.自定义测试器 P86下方| 我们创建了一个没有意义的baz过滤器 | 我们创建了一个没有意义的baz测试器 | 笔误 19.1.9 | 
| 4.3.1 P115 第 2 小节的代码块第 5 行 | `Length(8, 128)` | `Length(6, 128)` | 前后不一致（1-3 重印时需要反过来调整另外 3 处），18.12.28 |
| 5 P139 第 1 个代码块 | | `$ flask run` 上面添加一行 `$ flask initdb  # 初始化数据库，后面会详细介绍` | 疏漏 19.1.5 |
| 5.4.2 | P153 | 代码清单 5-5 | | 删掉第 3 行，最后一行删除括号中的`, form=form` | 代码未更新 18.12.24 |
| 5.4.2 | P155 | 代码清单 5-8 第 3 行 | `DeleteForm()` | `DeleteNoteForm()` | 代码未更新 18.12.24 |
| 7.3.1 | P207 | 3.7.1节中最后一段话中 | bootstrap_load_js() | bootstrap.load_js() | 笔误 18.11.17 |
| 7.4.3 | P213 | 最后 1 个附注段落 | bootstrap.bundle.min.css |  bootstrap.bundle.min.js | 笔误 18.12.5 |
| 7.5 P214 该页（节）最后 2 个代码块的最后 1 行 | | 两处均向左缩进 4 格，和上面对齐 | 排版错误 18.12.6 |
| 8.2.1 | P237 | 代码清单 8-8 倒数第 3 行 | | 添加注释：`# 这个方法将在 8.4.3（P273）节介绍` | 后续内容前置提示 18.12.6 |
| 8.3.5 | P264 | 图 8-8 上的代码块第2行 | `{{ comment.replied.author.name }}` | `{{ comment.replied.author }}` | 笔误 18.12.6 |
| 8.3.7 | P268 | 第1行 | photo | show_post | 笔误 18.12.6 |
| 8.4.1 | P273 | 纸书该页第 2 个代码块，电子书 8.4.2 上面倒数第 2 个代码块。第 5、7 行 | `check_password` | `validate_password` | 笔误 18.12.6 |
| 8.5.3 P278 代码清单8-37代码块第1行 | `from flask_login import logout_user` | `from flask_login import logout_user, login_required` | 代码错误 18.12.6 | 
| 8.7.1.2 P288 代码清单8-42代码块倒数第2行  | `.show_post` | `blog.show_post`  | 笔误 18.12.6 | 
| 8.7.1.3 P290 第1个代码块倒数第5行  | `.show_post` | `blog.show_post`  | 笔误 18.12.6 |
| 8.7.2 P292 代码清单8-44代码块倒数第1行  | `.show_post` | `blog.show_post`  | 笔误 18.12.6 | 
| 9.1.1 P301 该页最后 1 行，电子书该节第 2 个代码块最后一行 | | 向左缩进 4 格 | 排版错误 18.12.6 |
| 9.1.1 P302 9.1.2 标题上面的代码块 | `bluelog` | `myapp` | 笔误 18.12.6 |
| 9.3.2.1 P312 第二个代码块上正文倒数第1行 | Operations字典中 | Operations类中| 笔误 18.12.10 |
| 9.3.2.2 P314 代码清单9-6代码块最后1行 | `url_for('.reset_confirmation')` | `url_for('.reset_confirm_email')`| 笔误 18.12.12 |
| 9.4.4 P324 代码清单9-14代码块第4-5行 || 两处均向左缩进 4 格 | 排版错误  18.12.10 |
| 9.5.3 P334 9.6 小节上面的代码块最后一行模板字符串 | `home/upload.html` | `main/upload.html` | 遗留代码未更新 18.12.17 |
| 9.5.3 P334 9.6 小节上面的代码块 | | 代码中的 400 和 800 分别替换为配置变量 `current_app.config['ALBUMY_PHOTO_SIZE']['small']` 和 `current_app.config['ALBUMY_PHOTO_SIZE']['medium']` | 遗留代码 18.12.17 |
| 9.8.3 P363 代码清单9-45代码块倒数第6行 | `{% if collections %}` |`{% if collects %}`| 笔误 18.12.10 |
| 9.9.4 P371 代码清单9-53的路径 | albumy/templates/profile_popup.html | albumy/templates/main/profile_popup.html | 笔误 18.12.21 |
| 9.9.4 P375 代码清单 9-56 下面的代码块第二行 | id="followers-count" | id="followers-count-{{ user.id }}" | 笔误 18.12.21 |
| 9.11.2 P388 最后一行 | 渲染avatar.html模板 |渲染change_avatar.html模板| 笔误 18.12.10 |
| 9.11.2 P389 第一个代码块下正文第1行 | avatar.html模板继承自settings.html模板 |change_avatar.html模板继承自settings/base.html模板| 笔误 18.12.10 |
| 9.11.2 P389 代码清单9-71代码块第1行 | `{% extends 'user/settings.html' %}` |`{% extends 'user/settings/base.html' %}`| 笔误 18.12.10 |
| 9.11.6 P397 代码清单9-79代码块倒数第5行 | `db.session.delete(current_user)` |`db.session.delete(current_user._get_current_object())`| 笔误 18.12.10 |
| 9.11 P385 代码清单9-66倒数第9行 | `{{ render_nav_item('user.notification_setting', 'Notification and Privacy') }}` | `{{ render_nav_item('user.notification_setting', 'Notification') }} {{ render_nav_item('user.privacy_setting', 'Privacy') }}` | 代码与实际项目不符 18.12.24 |
| 9.11.2 P389 代码清单9-71倒数第4行 | `{{ render_form(crop_form) }}` | `{{ render_form(crop_form, action=url_for('.crop_avatar')) }}` | 笔误 18.12.24 |
| 9.14.3 P412 代码清单9-90 | | | 缺少validate_username()方法的定义 18.12.24 |
| 10.1.1 P420 第 2 小节第一个代码块第 7 行 | `{{ url_for('todo.clear_item') }};` | `{{ url_for('todo.clear_items') }};` | 笔误 18.12.27 |
| 10.3.3 P447 第 1 小节/该页最后一个代码块 | `... import api` | `... import api_v1` | 笔误 18.12.28 |
| 10.3.3 P447 第 1 小节/该页最后一个代码块 | `csrf.exempt(api)` | `csrf.exempt(api_v1)` | 笔误 18.12.28 |
| 10.3.3 P453 代码清单10-13第一行中的methods参数 | `methods=['GET', 'POST']` | `methods=['GET']` | 与原定的方法不一致 18.12.28 |
| 10.3.3 P453 代码清单10-13第二行中的第一个参数 | `'/token'` | `'/oauth/token'` | 与实际项目不一致 18.12.28 |
| 10.3.3 P453 代码清单10-13第二行中的methods参数 | `methods=['GET']` | `methods=['POST']` | 与实际项目不一致 18.12.28 |
| 10.3.5 P462 代码清单10-20倒数第4行 | `'username': item.author,` | `'username': item.author.username,` | 笔误 18.12.28 |
| 11.3.2 P483 代码清单11-4倒数第2行 | | 花括号"}"后添加一个逗号"," | 笔误 18.12.28 |
| 11.3.2 P484 代码清单11-5第2行 | `$('message').append(data.message_html);` | `$('.messages').append(data.message_html);` | 笔误 18.12.28 |
| 11.4.1 P491 该节最后一段正文的第1行 | views包 | blueprints包 | 笔误 18.12.29 |
| 11.4.3 P498 附注段落下方正文第2行 | provide_name | provider_name | 笔误 18.12.29 |
| 11.4.3.5 P503 最后一个代码块 | `access_token = resp.get('access_token')` | `access_token = response.get('access_token')` | 笔误 18.12.29 |
| 11.4.3.6 P505 提示段落上方的代码块 | `@oauth_bp.route(...)` | `@auth_bp.route(...)` | 笔误 18.12.29 |
| 11.4.4 P506 第二个代码块 | 所有resp | response | 笔误 18.12.29 |
| 11.4.4 P506 第二个代码块 | | 增加if response is not None:... else:...语句，具体参考源码 | 笔误 18.12.29 |
| 11.5.1 P508 代码清单11-12 | `return render_template('_messages.html', messages=messages[::-1])` | `return render_template('chat/_messages.html', messages=messages[::-1])` | 笔误 18.12.29 |
| 11.5.1 P509 代码清单11-13第5行 | `position === 0&& socket.nsp! == '/anonymous'` | `position === 0 && socket.nsp !== '/anonymous'` | 审校错误，空格错误 18.12.29 |
| 11.5.1 P510 代码清单11-13倒数第6行 | `toast('No more messages.');` | `alert('No more messages.');` | 此项目中未定义toast函数 18.12.29 |
| 11.5.4 P516 代码清单11-15第3行 | `socket.on('message', function (data) {` | `socket.on('new message', function (data) {` | 笔误 18.12.29 |
| 11.5.4 P516 代码清单11-15第6行 | `document.title = '(' + message_count + ') ' + document.title;` | `document.title = '(' + message_count + ') ' + 'CatChat';` | 消息数量会随着事件多次发生而不断追加在原标题前 18.12.29 |
| 11.5.5 P517 代码清单11-17第6行 | `data.name` | `data.nickname` | 笔误 18.12.30 |
| 11.5.5 P517 代码清单11-17第7行 | `icon: ...` | `icon: data.gravatar` | 笔误 18.12.30 |
| 11.5.5 P518 最后1个代码块第5行 | `render_template('_message.html', message=message)` | `render_template('chat/_message.html', message=message)` | 笔误 18.12.30 |
| 11.5.5 P518 最后1个代码块第6行 | `message_body` | `html_message` | 笔误 18.12.30 |
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
| 16.2.4 P639 最后1个段落的第2行 | 在不基于线程、greenlet或单进程实现的并发服务器上 | 在不基于线程、Greenlet 或进程实现并发的服务器上 | 笔误 18.12.31 |
| 16.4.2 P649 最后1行| Flask.route()是Flask类的类方法 | Flask.route()是Flask类的实例方法 | 笔误 19.1.1 |
| 16.4.3 2. 堆栈与LocalStack  P659 第1段第3行| 并将数据的字典名称设为'stack'。| 并将储存上下文对象的列表名称设为'stack' | 笔误 19.1.4 |

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
| 3.4.2 P97 注意段落最后一行 | Boostrap | Boo**t**strap | 笔误 18.12.28 |
| 3.4.4 P101 图 3-5 下面第 1 行文字 | 处理器和模块 | 处理器和模**板** | 笔误 19.1.13 |
| 4.4.4.1 P123 代码清单4-13第3行 | | 字符间距过大。 | 排版错误 19.1.5 |
| 4.4.5.2 提示段落 | https://flask-ckeditor.readthedocs.io/configuration.html | https://flask-ckeditor.readthedocs.io/en/latest/configuration.html | 笔误 19.1.5 |
| 5.5.2 | P160 | 正文最后一行、P161 第一行 | Aritcle | Article | 笔误 18.12.24 |
| 7.2.3 P204 代码清单7-5后面的代码块第4行 | | `messages = Message.query.order_by...`向后缩进1格 | 缩进 19.01.11 |
| 7.5 P213 最后一行代码 | `fake = Faker('zh_CN'))` |  `fake = Faker('zh_CN')` | 笔误 18.11.17 |
| 8.2.1 P239 代码清单 8-12 文件路径 | bluelog/commands.py | bluelog/__init__.py | 遗留代码未更新 19.1.13 |
| 8.3.5 | P265 | 第1个代码块倒数第11行 | `Reply</a>` | `Reply</a></div>` | 笔误 18.12.6 |
| 8.7.2.2 P294 代码清单8-45代码块下正文第1行  | `Ture` | `True`  | 笔误 18.12.6 | 、
| 8.5 P276 提示上方段落第一行 | UserMinxin | UserMixin | 笔误 18.12.23 |
| 8.5.3 P279 代码清单 8-37 第 4 行 | @login_required | @login_required  # 用于视图保护，后面会详细介绍 | 添加注释 19.1.5 |
| 9.2 P310 代码清单9-3代码块第7行 | `url_for ('main.index')` |`url_for('main.index')`| 笔误 18.12.10 |
| 9.8.2 P360 代码清单9-41代码块上访正文倒数第3行 | 实际动作是有用户做出的| 实际动作是由用户做出的| 笔误 18.12.10 |
| 9.9.1 P365 9.9.1 标题下正文第一行 | Uesr | User | 笔误 18.12.21 |
| 9.9 P365 代码清单9-47下方的正文 | timastamp | timestamp | 笔误 18.12.21 |
| 9.7.1 P340 代码清单 9-24 第 2 处注释 | 主要 | 主页 | 笔误 18.12.17 |
| 9.2 P304 图9-1左上角多了一个"搜索" | `搜索` | 去掉一个`搜索` | 笔误 18.12.10 |
| 9.11.2 P388 提示下方的正文 | Scripts块 | scripts块 | 笔误 18.12.24 |
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
| 16.4.3 3.代理与LocalProxy P660 Cython交互代码片段第8第9行| 代码与第6第7行重复，可删除 | 校对错误 | 19.1.7 |
| 16.4.5 P669 代码清单16-28 多行注释| 一个字典，每当产生改变化时会调用传入的参数 | 一个字典，每当产生变化时会调用传入的参数 | 笔误 19.1.9 |

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
