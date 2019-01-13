[主页](https://github.com/greyli/helloflask)
/ 勘误
/ [FAQ](https://github.com/greyli/helloflask/blob/master/faq/faq.md)
/ [可改进实现](https://github.com/greyli/helloflask/blob/master/improvement/improvement.md)
/ [版本更新记录](https://github.com/greyli/helloflask/blob/master/CHANGES.md)
/ [示例程序](https://github.com/greyli/helloflask/blob/master/demos/)
/ [HelloFlask.com](http://helloflask.com)
/ [本书主页](http://helloflask.com/book)

# 勘误

**请访问 http://helloflask.com/book/errata 阅读勘误**，这里是勘误源码。

如果你发现了书中的错误，欢迎提交PR更新勘误文件；你也可以创建Issue指出相关错误，或是通过Email与我联系（[withlihui@gmail.com](mailto:withlihui@gmail.com)），谢谢！

最后更新：2019/01/06

## 勘误贡献者列表

统计时间：2018/12/28

* @JustALee https://github.com/JustALee
* @meizhaohui 梅朝辉 https://github.com/meizhaohui
* @AngelLiang 阏男秀 https://github.com/AngelLiang
* @jiangyanglinlan https://github.com/jiangyanglinlan
* @BobcatsII Pandalis https://github.com/BobcatsII
* @vimiix Vimiix-Yao https://github.com/vimiix
* @SnailZSJ 张树杰 https://github.com/SnailZSJ
* @hjlarry 非法操作 https://github.com/hjlarry
* @kaka4NERV xiewei https://github.com/kaka4NERV
* @NPUTom 张万强 https://github.com/NPUTom
* @jpch89 进击的团子 https://github.com/jpch89
* @山野村夫 https://www.zhihu.com/people/henry-1-97/
* @RYLF RuoYun https://github.com/RYLF
* @python012 Reed Xia https://github.com/python012
* @litt1eseven Little student. https://github.com/litt1eseven
* @sangjianfeng sangjf https://github.com/sangjianfeng
* @xm-y xmyang https://github.com/xm-y
* @zerosail https://github.com/zerosail
* @VladCraste Vlad Craste https://github.com/VladCraste
* @Abyssknight Glory Guan https://github.com/Abyssknight
* @hallucigenia https://github.com/hallucigenia
* @libincla https://github.com/libincla
* @stravel611 https://github.com/stravel611
* @Merpyzf wang ke https://github.com/Merpyzf
* @realzhangm Colin Zhang https://github.com/realzhangm
* @candycrusher Jiayu Song https://github.com/candycrusher
* @xxiaocheng Chengxiao https://github.com/xxiaocheng
* ……

另外还有通过 QQ、Telegram 和 Email 反馈勘误的读者，不方便索引，这里没有一一列出。感谢你们的贡献！


## 纸书

纸书的版本号格式为“版本号-印次号”，“1-1”即“第一版第一次印刷”。**每一次重印会修正上一印次包含的所有错误**，版本号可以在版权页看到。

### 1-1

发布时间：2018/9/1

#### 重要勘误

此处的勘误为会影响程序运行和理解的错误，需要在阅读前标记到书上，以免影响阅读。

位置 | 错误 | 正确 | 备注/时间 |
--- | --- | --- | ---
| 1.2.2.2 P13 代码清单1-3下第2段第2行 | http://helloflask.com/hello/Grey | http://helloflask.com/greet/Grey | 笔误 |
| 1.7 P23 第2个代码块下第1行 | `url_for('say_hello', name='Jack')` | `url_for('greet', name='Jack')` | 笔误 |
| 2.2.1 P31 表2-3左侧下面的两行 | | POST对应的说明列原文为“传输数据”，修改为“创建或更新资源”；PUT对应的说明列原文为“传输文件”，修改为“创建或替换资源” | 改进 18.11.18 |
| 2.2.3.3 P36 表2-6后第1个代码块 | `'goback/<int:year>'` | `'/goback/<int:year>'` | 笔误。 18.9.28 |
| 2.3.1 P40 第3个代码块 | `{'Location', 'http://www.example.com'}` | `{'Location': 'http://www.example.com'}` | 笔误。返回值中字典里的符号出错 |
| 2.3.2 P44 HTML小节的最后1行 | HTTP | HTML | 笔误 |
| 2.3.2.4 P46 倒数第3个代码块 | `return jsonify({name: 'Grey Li', gender: 'male'})` | `return jsonify({'name': 'Grey Li', 'gender': 'male'})` | 笔误。字典键加引号 18.10.18 |
| 2.2.3 P48 图2-11 |  | 图中的响应状态码应该为 302 Found | 文图不对应 18.10.18 |
| 2.3.4.2 P50 代码清单2-5下第1段第3行 | logged-in cookie| logged_in cookie | 排版错误 18.11.8 |
| 2.3.4.2 P51 图2-12后第1个代码块 | | 第9行及以下均应向左缩进4个空格 | 排版错误 18.10.18 |
| 2.3.4.2 P52 图2-13后第1段第2行 | logged-in | logged_in | 排版错误 18.11.8 |
| 2.3.4.2 P52 代码清单2-6下第2段第2行  | logged-in | logged_in | 排版错误 18.11.8 |
| 2.5.4.1.(2) P67 “攻击示例”小节第3段文字第2行 | 设为 “';drop table users; --” | 设为 “';drop table students; --” | 笔误 18.11.2 |
| 4.2.3 P110 代码清单4-2最后1行 | `'login.html'` | `'basic.html'` | 笔误 18.9.28 |
| 4.3.1 P112 第1个代码块后第1行 | 3000 | 2000 | 笔误，不同的浏览器对于URL有不同的长度限制，此处长度为“最佳实践” |
| 4.3.1 P113 代码清单4-5第1行 | `'/'` | `'/basic'` | 笔误 18.10.18 |
| 4.3.1 P115 第 2 小节的代码块第 5 行 | `Length(8, 128)` | `Length(6, 128)` | 前后不一致（1-3 重印时需要反过来调整另外 3 处），18.12.28 |
| 4.4.4.3.(3)第6个代码块下正文第2行 P127第2个代码块下正文第2行 | | 这个uploads视图 | 这个get_file视图 | 笔误 18.10.27 |
| 4.4.4.4 P128 代码清单4-16 | | “检查文件类型”注释下第一行多余缩进4格 | 笔误 18.10.18 |
| 5 P139 第 1 个代码块 | | `$ flask run` 上面添加一行 `$ flask initdb  # 初始化数据库，后面会详细介绍` | 疏漏 19.1.5 |
| 5.4.1.1 P147 ”Create“小节第1个代码块第4行 | `'DON'T BELIEVE……'` | `'DON\'T BELIEVE……'` | 代码错误，漏掉转义符号 |
| 5.4.1.2 P150 表5-7下的第1个代码块 | `Note.body='SHAVE'` | `Note.body == 'SHAVE'` | 代码错误，少了1个等号 18.9.22 |
| 5.4.2 P153 代码清单 5-5 | | 删掉第 3 行，最后一行删除括号中的`, form=form` | 代码未更新 18.12.24 |
| 5.4.2 P155 代码清单 5-8 第 3 行 | `DeleteForm()` | `DeleteNoteForm()` | 代码未更新 18.12.24 |
| 5.5.2.3 P160 ”建立关系“小节第1个代码块 | | 第2行插入`ham.author_id = 1` | 省略步骤，可加可不加 18.9.22 |
| 5.5.2.4 P162 代码清单5-11第8行 | `title = ` | `name = ` | 笔误 18.9.26 |
| 5.5.2.4 P163 ”建立双向关系“小节第3个代码块第6行 | `it.writer = writer` | `it.writer = king` | 笔误 18.9.26 |
| 5.5.3 P164 代码清单5-13上面 | 都定义在“多”这一侧，即City类中 | 都定义在“多”这一侧，即Citizen类中 | 笔误 |
| 5.5.4 P165 代码清单5-14后面的代码块第6行 | - | 第6行`>>> china.capital = beijing`移动到第3行 | 笔误 |
| 5.5.4 P165 代码清单5-14后面的代码块第8行 | `<Capital 1>` | `<Capital u'Beijing'>` | 笔误 |
| 5.5.4 P166 代码清单5-14后面的代码块第10行，166页第2行 | `u'China'` | `<Country u'China'>` | 笔误 |
| 5.5.4 P166 代码清单5-14后面的代码块第11行，166页第3行 | `name'Tokyo'` | `name='Tokyo'` | 笔误 18.9.26 |
| 5.7.1.2 P174 ”delete-orphan“小节上面第1个代码块第1行 | `Post.quer2y.get(2)` | `Post.query.get(2)` | 审校错误 |
| 5.7.2 P176 代码清单5-18下第1行 | targe | target | 笔误 18.9.28 |
| 5.7.2 P177 最后1个代码块上面 | 参数name | 参数named | 笔误 18.9.28 |
| 5.7.2 P177 最后1段提示文字 | 监听函数时， | 监听函数。这时 | 编辑瞎改稿子 18.9.28 |
| 5.7.2 全章节多处 | listen_for | listens_for | 笔误 18.9.28 |
| 6.1.1 P181 代码清单6-1 | | 第9-13行末尾漏掉分割参数的逗号 | 笔误 18.10.27 |
| 7.3.2 P208 第1个代码块第6行 | `render_form(form),action=request.full_path` | `render_form(form, action=request.full_path)` | 审校错误，右侧关闭括号位置出错 |
| 7.3.2 P208 表7-2上面段落的最后一句话 | quick_form() | render_form() | 笔误。历史遗留问题 18.9.28 |
| 7.4.3 P213 最后 1 个附注段落 | bootstrap.bundle.min.css |  bootstrap.bundle.min.js | 笔误 18.12.5 |
| 8.1.3 P229、P231 代码清单8-2、8-4 | | 单个蓝本变量名称均应为foo_bp形式，比如admin应为admin_bp | 笔误 18.9.24 |
| 8.2.1.1.(4) P235 代码清单8-7后面第1个代码块第3行 | `db.relationship('Comment', backref='post', cascade='all')` | `db.relationship('Comment', back_populates='post', cascade='all, delete-orphan')` | 笔误 |
| 8.2.3 P247 代码清单8-19第2行 | `from wtforms` | `from wtforms.validators` | 笔误 18.10.27 | 
| 8.3.1 P252 第1个代码块最后1行 | `'index.html'` | `'blog/index.html'` | 笔误 18.10.06 |
| 8.3.1 P252 代码清单8-24文件路径 | templates/index.html | templates/blog/index.html | 笔误 18.10.06 |
| 8.3.5 P263 第1个代码块第6行 | `Comment.query.with_parent(post)` | `Comment.query.with_parent(post).filter_by(reviewed=True)` | 笔误 18.9.26 |
| 8.3.5 P264 代码清单 8-29 倒数第11行 | `Reply</a>` | `Reply</a></div>` | 笔误 18.12.6 |
| 8.3.5 P265 图 8-8 上的代码块第2行 | `{{ comment.replied.author.name }}` | `{{ comment.replied.author }}` | 笔误 18.12.6 |
| 8.3.7 P267 代清清单8-31第4行 | `comment.photo_id` | `comment.post_id` | 笔误 18.9.26 |
| 8.3.7 P267 代清清单8-31下方正文第2段最后一行的URL中 | photo | post | 笔误 18.9.26 |
| 8.3.7 P268 第1行 | photo | show_post | 笔误 18.12.6 |
| 8.4.1 P272 第1个代码块最后1行 | `>>> False` | `>>> True` | 笔误 18.10.27 |
| 8.4.1 P273 纸书该页第 2 个代码块，电子书 8.4.2 上面倒数第 2 个代码块。第 5、7 行 | `check_password` | `validate_password` | 笔误 18.12.6 |
| 8.5 P275 “8.5”小节下第2个代码块第2行 | `LoginManager(app)` | `LoginManager()` | 代码错误 18.12.23 | 
| 8.5.3 P278 代码清单8-37代码块第1行 | `from flask_login import logout_user` | `from flask_login import logout_user, login_required` | 完善导入 18.12.6 | 
| 8.6 P282 代清清单8-38第4行 | `'400.html'` | `'errors/400.html'` | 笔误 18.10.27 |
| 8.7.1 P285 代码清单8-40下的正文第1行 | manage_category.html | manage_post.html | 笔误 18.10.27 | 
| 8.7.1.2 P288 代码清单8-42代码块倒数第2行  | `.show_post` | `blog.show_post`  | 笔误 18.12.6 | 
| 8.7.1.3 P290 第1个代码块倒数第5行  | `.show_post` | `blog.show_post`  | 笔误 18.12.6 |
| 8.7.2 P292 代码清单8-44代码块倒数第1行  | `.show_post` | `blog.show_post`  | 笔误 18.12.6 | 
| 8.7.2.2 P294 代码清单8-45代码块下正文第1行  | `Ture` | `True`  | 笔误 18.12.6 | 
| 9.1.1 P302 9.1.2 标题上面的代码块 | `bluelog` | `myapp` | 笔误 18.12.6 |
| 9.3.2.2 P314 代码清单9-6代码块最后1行 | `url_for('.resend_confirmation')` | `url_for('.resend_confirm_email')`| 笔误 18.12.12 |
| 9.3.3 P315 代码清单9-8下的正文第2段第2行（纸书该页最后1行） | `auth.resend_confirmation` | `auth.resend_confirm_email` | 笔误 18.11.5 |
| 9.5.3 P334 9.6 小节上面的代码块最后一行模板字符串 | `home/upload.html` | `main/upload.html` | 遗留代码未更新 18.12.17 |
| 9.5.3 P334 代码清单9-19后面的代码块倒数第二行 | `photo.save()` | `db.session.add(photo) 换行 db.session.commit()` | 遗留代码未更新 18.10.27 |
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
| 10.3.6.3 P468 ”处理错误响应“小节第1行 | app.error_handler | app.errorhandler | 笔误 |
| 11.3.2 P483 代码清单11-4倒数第2行 | | 花括号"}"后添加一个逗号"," | 笔误 18.12.28 |
| 11.3.2 P484 代码清单11-5第2行 | `$('message').append(data.message_html);` | `$('.messages').append(data.message_html);` | 笔误 18.12.28 |
| 11.4.1 P491 该节最后一段正文的第1行 | views包 | blueprints包 | 笔误 18.12.29 |
| 11.4.3 P498 附注段落下方正文第2行 | provide_name | provider_name | 笔误 18.12.29 |
| 11.4.3.5 P503 代码清单11-11中多处 | `get['XXX']` | `get('XXX')` | 审校错误 |
| 11.4.3.5 P503 最后一个代码块 | `access_token = resp.get('access_token')` | `access_token = response.get('access_token')` | 笔误 18.12.29 |
| 11.4.3.6 P505 提示段落上方的代码块 | `@oauth_bp.route(...)` | `@auth_bp.route(...)` | 笔误 18.12.29 |
| 11.4.4 P506 第二个代码块 | 所有resp | response | 笔误 18.12.29 |
| 11.4.4 P506 第二个代码块 | | 增加 if response is not None:... else:...语句，具体参考源码 | 笔误 18.12.29 |
| 11.5.1 P508 代码清单11-12 | `return render_template('_messages.html', messages=messages[::-1])` | `return render_template('chat/_messages.html', messages=messages[::-1])` | 笔误 18.12.29 |
| 11.5.1 P509 代码清单11-13第5行 | `position === 0&& socket.nsp! == '/anonymous'` | `position === 0 && socket.nsp !== '/anonymous'` | 审校错误，空格错误 18.12.29 |
| 11.5.1 P510 代码清单11-13倒数第6行 | `toast('No more messages.');` | `alert('No more messages.');` | 此项目中未定义toast函数 18.12.29 |
| 11.5.3 P513~P514 513页7处，514页8处 |  | 所有的 Pyments 改为 Pygments，pyments 改为 pygments | 笔误 18.11.18 |
| 11.5.4 P516 代码清单11-15第3行 | `socket.on('message', function (data) {` | `socket.on('new message', function (data) {` | 笔误 18.12.29 |
| 11.5.4 P516 代码清单11-15第6行 | `document.title = '(' + message_count + ') ' + document.title;` | `document.title = '(' + message_count + ') ' + 'CatChat';` | 消息数量会随着事件多次发生而不断追加在原标题前 18.12.29 |
| 11.5.5 P517 代码清单11-17第6行 | `data.name` | `data.nickname` | 笔误 18.12.30 |
| 11.5.5 P517 代码清单11-17第7行 | `icon: ...` | `icon: data.gravatar` | 笔误 18.12.30 |
| 11.5.5 P518 最后1个代码块第5行 | `render_template('_message.html', message=message)` | `render_template('chat/_message.html', message=message)` | 笔误 18.12.30 |
| 11.5.5 P518 最后1个代码块第6行 | `message_body` | `html_message` | 笔误 18.12.30 |
| 12.3.1 P526 代码清单12-1 | | setUp方法最后面追加一行代码`self.client = app.test_client()` | 代码缺失 19.01.05 |
| 12.3.2 P527 提示段落下方的正文第3行 | assertEqual() | assertTrue() | 笔误 19.01.05 |
| 12.3.2 P527 代码清单12-3 test_404_page方法的注释 | # 测试 400 错误页面 | # 测试 404 错误页面 | 笔误 19.01.05 |
| 12.3.2.2 P532 正文第4个段落的最后1行 | JOSN | JSON | 笔误 19.01.05 |
| 12.3.2.3 P532 代码清单12-5 | `from sayhello.commands import forge` | `from sayhello.commands import forge, initdb` | 导入缺失 19.01.05 |
| 12.3.3 P533 代码清单12-6上方正文最后第2行 | tearDow() | tearDown() | 笔误 19.01.06 |
| 12.3.3 P534 代码清单12-6第2个导入语句 | `from flask import current_app, url_for` | `from flask import url_for` | 多余的导入 19.01.06 |
| 12.3.3 P534 代码清单12-6最后1个导入语句 | `from bluelog.models import User` | `from bluelog.models import Admin` | 笔误 19.01.06 |
| 12.3.3 P534 代码清单12-7第2个导入语句 | `from flask import current_app, url_for` | `from flask import url_for` | 多余的导入 19.01.06 |
| 12.4.3 P540 代码清单12-10中test_index方法中self.assertIn()的第1个参数 | 'Todoism makes everything clear.' | 'We are todoist, we use todoism.' | 遗留代码未更新 19.01.06 |
| 12.6 P546 第1个附注段落上方的正文第2行 | 弃用 | 启用 | 笔误 19.01.06 |
| 13.1.2 P550 代码清单13-1 | `@app.after_app_request` | `@app.after_request` | 笔误 19.01.06 |
| 13.1.2 P550 代码清单13-1 | | 两处current_app改为app | 笔误 19.01.06 |
| 13.3 P557 第2个提示段落 | CND | CDN | 笔误 19.01.06 |
| 13.3 P557 命令行命令 | `$ cd cache` | `$ cd assets` | 笔误 19.01.06 |
| 13.3.3 P560 第1段正文第3行 | style块 | styles块 | 笔误 19.01.06 |
| 15.7.3 P625 最后1个代码块的第2行 | `git push origm` | `git push origin` | 审校错误。另外，这一行下面的Github应为GitHub |
| 16.2.4 P639 最后1个段落的第2行 | 在不基于线程、greenlet或单进程实现的并发服务器上 | 在不基于线程、Greenlet 或进程实现并发的服务器上 | 笔误 18.12.31 |
| 16.4.3  2. 堆栈与LocalStack  P659 第1段第3行| 并将数据的字典名称设为'stack'。| 并将储存上下文对象的列表名称设为'stack' | 笔误 19.1.4
| 16.4.2 P649 最后1行| Flask.route()是Flask类的类方法 | Flask.route()是Flask类的实例方法 | 笔误 19.1.1 |

#### 不重要勘误

此处的勘误多为单词拼写错误或不影响理解和程序运行的笔误，可以忽略。

位置 | 错误 | 正确 | 备注/时间 |
--- | --- | --- | ---
| 全局 | 单击 | 点击 | 审校错误。多处。编辑称这个修改是出版社的规范要求，我觉得有些莫名其妙 |
| 全局 |  | 代码块中的英文单词换行被截断时错误的添加的连接线 | 排版错误。多处，详情见下面的列表 |
| 全局 | Github | GitHub | 大小写错误。多处 |
| 前言 V 本书主要特点中的第2点 | 第一部分的2~6章 | 第一部分的1~6章 | 审校错误 |
| 前言 V 本书主要特点中的第3点 | Pyhton | Python | 拼写错误 |
| 前言 V 本书主要特点中的第3点 | Boostrap | Bootstrap | 审校错误 |
| 前言 X 排版约定最后一段的上面1行 | you_email| your_email | 拼写错误 |
| 1.2 P11 代码清单1-1下的提示文字 | 命令为 | 命名为 | 笔误 |
| 1.2.2 P13 标题1上面的附注段落 | Lacator | Locator | 拼写错误 18.10.25 |
| 1.3.1 P14 标题 | Run，Flask，Run！ | Run, Flask, Run! | 标点错误 |
| 1.3.1 P14 ”Run，Flask，Run“小节第1个代码块最后1行 | | 出现多余的缩进 | 排版错误 |
| 1.3.1.3 P17 配置步骤4 | 下列选项 | 下拉选项 | 笔误 |
| 1.3.3 P18 ”1.3.3“小节第1行 | Enviroment  | Environment | 拼写错误 |
| 2.2.2 P33 正文第一行 | MutliDict | MultiDict | 笔误 18.12.24 |
| 2.2.2 P33 图 2-4 上面一行 | requset | request | 笔误 18.12.28 |
| 2.2.2 P33 代码清单 2-1 最后一行 | `'<h1>Hello, %s!<h1>'` | `'<h1>Hello, %s!</h1>'` | `<h1>` 关闭斜线 18.12.28 |
| 2.2.2 P33 代码清单 2-1 最后一行 | | 该行注释缩进出错，向左移动至保留 2 个空格 | 排版错误 18.12.28 |
| 2.2.3 P34 图2-5 |  | 地址栏的地址应为/nothing，和描述对应。图中的/foo在后面实际被定义了 | 笔误 18.9.28 |
| 2.3.1 P41 代码清单 2-2 第 7 行 | redierct | redirect | 笔误 18.12.24 |
| 2.3.2.4 P45 JSON代码示例 | "heading":"Remider", |  "heading":"Reminder",  | 笔误。单词拼写错误。 18.11.28 |
| 2.3.3 P47 表2-10后面的第1个附注段落 | Respone | Response | 笔误。拼写错误 |
| 2.5.4.1.(2) P67 纸书该页第1个代码块，电子书“攻击示例”小节第2个代码块 |  | 最后的单引号和前面的分号对调位置 | 笔误 18.11.5 |
| 2.5.4.1.(2) P67 纸书该页第2个代码块，电子书“攻击示例”小节第3个代码块 |  | 在最后的分号前添加一个半角单引号 | 笔误 18.11.5 |
| 2.5.4.1.(3) P67 ”主要防范方法“小节第1个代码块 | `db.execute('SELECT * FROM students WHERE password=?, password)` | `db.execute('SELECT * FROM students WHERE password=?', password)` | 笔误。字符串右侧引号 |
| 2.5.4 P69 纸书该页最后1行的代码块最后几个字符 | `sript` | `script` | 笔误 18.11.5 | 
| 3.1.1 P76 代码清单 3-1 文件路径 | template/watchlist.html | template**s**/watchlist.html | 笔误 18.12.28 |
| 3.1 P77 代码清单3-1下的提示 | HTML5 | HTML | 多余文本。另外，后面的链接需要更新为 https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure |
| 3.2.5 P87 正文共 5 处 | enviroment | enviro**n**ment | 拼写错误 18.12.28 |
| 3.3.2 P89 第1个代码块上面的文字第2行 | `_macors.html` | `_macros.html` | 笔误 |
| 3.3.2 P89 第1个注意段落最后1行 | 显示 | 显式 | 笔误 18.10.18 |
| 3.4.1 P93 第1~4个代码块 | | 忽略了 Jinja 本身的代码逻辑，读者可忽略 Jinja 语句含义 | 逻辑错误。 18.11.5 |
| 3.4.2 P97 注意段落下面正文第2行 | CND | CDN | 笔误 18.10.27 |
| 3.4.2 P97 注意段落最后一行 | Boostrap | Boo**t**strap | 笔误 18.12.28 |
| 3.4.4 P101 图3-5 | | 地址栏的地址应为/nothing，和描述对应。 | 笔误 18.10.1 |
| 4.1 P105 最后一行 | ， | 。 | 笔误 18.11.11 |
| 4.2.1 P108 表4-3下面的注意段落 | `内置的验证器通过……` | `内置的验证器使用……` | 改善措辞 18.11.5 |
| 4.2.3 P110 代码清单4-3第3行 | `{{ from.username.label }}{{ form.username }}<br>` | `{{ from.username.label }}<br>{{ form.username }}<br>` | 改进 18.11.5 |
| 4.2.3 P110 代码清单4-3第4行 | `{{ from.password.label }}{{ form.password }}<br>` | `{{ from.username.label }}<br>{{ form.username }}<br>` | 改进 18.11.5 |
| 4.3.3 P117 代码清单4-7第4行 | `form.username()` | `form.username` | 笔误。此处的括号可有可无，去掉以保持风格上的统一 18.9.24 |
| 4.4.4.1 P123 代码清单4-13第1行 | `flask wtf` | `flask_wtf` | 审校错误 18.9.24 |
| 4.4.4.4 P128 代码清单4-16上面的第1个代码块第3行 | | 缺少右侧关闭括号 | 笔误 18.10.18 |
| 4.4.4.1 P123 代码清单4-13第3行 | | 字符间距过大。 | 排版错误 19.1.5 |
| 4.4.5.2 提示段落 | https://flask-ckeditor.readthedocs.io/configuration.html | https://flask-ckeditor.readthedocs.io/en/latest/configuration.html | 笔误 19.1.5 |
| 4.4.5 P131 代码清单4-19下正文段落第3行 | `Ture` | `True` | 笔误 18.11.5 |
| 5.3.1 P143 表5-2最后1行 | SQlite | SQLite | 大小写错误 18.10.27 |
| 5.3.3 P146 第2个代码块 | | 开头可添加一行导入`from app import Note` | 更完善 18.10.18 |
| 5.5.2 P159 表5-4下的注意段落第2行 | Flask-SQLlchemy | Flask-SQLAlchemy | 笔误 18.10.27 |
| 5.5.2 P160 正文最后一行、P161 第一行 | Aritcle | Article | 笔误 18.12.24 |
| 5.8 P177 最后1行 | 本章要介绍的 | 本章介绍的 | 笔误 18.9.28 |
| 6.1.3 P183 代码清单6-3第9行 | `return redirect(url_for('idnex'))` | `return redirect(url_for('index'))` | 笔误 18.10.27 |
| 6.2 P183 6.2及6.2.1章节标题以及目录共**4处** | SendGird | SendGrid | 笔误 18.10.27 |
| 7.2.3.1 P202 代码清单7-3的文件路径 | sayhello.py | models.py | 笔误 |
| 7.3.1 P207 3.7.1节中最后一段话中 | bootstrap_load_js() | bootstrap.load_js() | 笔误 18.11.17 |
| 7.4.3 P211 表7-4下面的提示段落 | https://momentjs.com/docs/displaying/format/ | https://momentjs.com/docs/#/displaying/format/ | 链接变化 18.11.5 | 
| 7.5 P213 最后一行代码 | `fake = Faker('zh_CN'))` |  `fake = Faker('zh_CN')` | 笔误 18.11.17 |
| 7.5 P214 该页（节）最后 2 个代码块的最后 1 行 | | 两处均向左缩进 4 格，和上面对齐 | 排版错误 18.12.6 |
| 8.1 P220 文件目录树 | | 目录树漏掉了 __init__.py 文件 | 笔误。 18.10.1 |
| 8.1.3 P229 第2个提示段落 | 新创建的模块 | 新创建一个模块 | 审校错误。 18.9.24 |
| 8.2.1 P237 代码清单 8-8 倒数第 3 行 | | 添加注释：`# 这个方法将在 8.4.3（P273）节介绍` | 后续内容前置提示 18.12.6 |
| 8.2.1.3 P237 代码清单8-9第10行 | | 缩进少一格 | 排版错误 18.10.18 |
| 8.3.3 P261 代码清单8-27 | | `<div class="modal-body">` 所在的行以及下面2行均向右缩进8格 | 排版错误 18.11.5 |
| 8.3.5 P264 代码清单8-29第12行 | `(%Y-%m-%dT%H:%M:%SZ')` | `('%Y-%m-%dT%H:%M:%SZ')` | 笔误，漏掉左侧引号 18.10.27 |
| 8.5 P276 提示上方段落第一行 | UserMinxin | UserMixin | 笔误 18.12.23 |
| 8.5.3 P279 代码清单 8-37 第 4 行 | @login_required | @login_required  # 用于视图保护，后面会详细介绍 | 添加注释 19.1.5 |
| 8.7.2.1 P293 图8-16上面的提示段落 | HTmL | HTML | 审校错误，大小写错误 |
| 9.1.1 P301 该页最后 1 行，电子书该节第 2 个代码块最后一行 | | 向左缩进 4 格 | 排版错误 18.12.6 |
| 9.2 P304 图9-1左上角多了一个"搜索" | `搜索` | 去掉一个`搜索` | 笔误 18.12.10 |
| 9.2 P310 代码清单9-3代码块第7行 | `url_for ('main.index')` |`url_for('main.index')`| 笔误 18.12.10 |
| 9.3.2.1 P312 第二个代码块上正文倒数第1行 | Operations字典中 | Operations类中| 笔误 18.12.10 |
| 9.4.4 P324 代码清单9-14代码块第4-5行 || 两处均向左缩进 4 格 | 排版错误  18.12.10 |
| 9.5.3 P334 9.6 小节上面的代码块 | | 代码中的 400 和 800 分别替换为配置变量 `current_app.config['ALBUMY_PHOTO_SIZE']['small']` 和 `current_app.config['ALBUMY_PHOTO_SIZE']['medium']` | 遗留代码 18.12.17 |
| 9.7.1 P340 代码清单 9-24 第 2 处注释 | 主要 | 主页 | 笔误 18.12.17 |
| 9.8.2 P360 代码清单9-41代码块上方正文倒数第3行 | 实际动作是有用户做出的 | 实际动作是由用户做出的| 笔误 18.12.10 |
| 9.9 P365 代码清单9-47下方的正文 | timastamp | timestamp | 笔误 18.12.21 |
| 9.9.1 P365 9.9.1 标题下正文第一行 | Uesr | User | 笔误 18.12.21 |
| 9.10.1 P379 代码清单9-59下面的代码块 | | 第2行向右缩进1格，第3行向左缩进，和第2行对齐。 | 排版错误 18.11.18 |
| 9.13 - 9.13小节最后代码清单上面的文字 | innit_app() | init_app() | 笔误 18.11.04 |
| 9.11.2 P388 提示下方的正文 | Scripts块 | scripts块 | 笔误 18.12.24 |
| 10.1 P417 项目结构示意图 | | blueprints下的__init__.py多缩进了 4 格 | 排版错误 18.12.27 |
| 10.2.2 P427 倒数第5行 | ISO 639?1 | ISO 639-1 | 笔误 18.12.28 |
| 10.2.4 P434 第 2 小节注意段落上方的正文段落的第一行 | message.po | messages.po | 笔误 18.12.28 |
| 10.2.4 P436 图10-3下方的正文第二行 | message.po | message**s**.po | 笔误 18.12.28 |
| 10.3.1 P442 倒数第5行 | Simple Object Acsess Protocol | Simple Object **Access** Protocol | 笔误 18.12.28 |
| 10.3.3 P446-P447 目录结构示意图 | | v1包下的4个模块少缩进一级，且apis子包缺少__init__.py模块 | 排版错误 18.12.28 |
| 10.3.4 P454 第二段正文的第二行 | Isssue | Issue | 笔误 18.12.28 |
| 10.2.5 P438 标题上面的附注文字 | 生成帮助信息 | 生成的帮助信息 | 审校错误。编辑以为自己在改病句，实际上却是在制造病句 |
| 10.3.1.4 P443 “10.3.2”小节上面段落倒数第3行 | RSET | REST | 笔误 |
| 10.3.3.5 P453 代码清单10-13下面的提示段落最后1行 | flask-restless | Flask-Restless | 大小写错误 |
| 11.1 P476 目录结构示意图 | | blueprints目录向左缩进一级 | 笔误 18.12.28 |
| 11.4.4 P507 正文第一行 | ture | true | 笔误 18.12.29 |
| 12.3.2 P527 代码清单12-2第7行 | test_app_exsit | test_app_exist | 拼写错误 |
| 14.3.1 P567 第二个代码块第2行| `token_urlsafe(16)` |  `secrets.token_urlsafe(16)` | 笔误 18.11.28 |
| 14.3.4 P569 代码清单14-1 register_logger函数缺少app参数| `register_logging()` |  `register_logging(app)` | 笔误 18.11.28 |
| 14.4.2 P574 第2个提示段落上面两处 | python(3) | python3 | 审校错误 |
| 14.4.7 P584 倒数第2个代码块上方段落第5行| 放在/etc/supervisord.conf路径下 | 放在/etc/supervisor/conf.d路径下 | 笔误 18.11.28 |

拼写错误，全书多处：Crtl 改为 Ctrl，下面是已知的错误位置：
P300 注意段落
P220 注意段落
P195 第二个注意段落
P416 注意段落
P475 注意段落
P15 正文第 1 行
P20 提示段落上面
P21 提示段落中两处
P577 页面中部两处
P580 页面中部
P584 页面中部

关于URL长度限制的详情可以参考[WWW FAQs: What is the maximum length of a URL?](https://www.boutell.com/newfaq/misc/urllength.html)。

## 源码错误

此处列出书中没有涉及的程序代码错误，目前临时在master分支更新，后续会重写相应的标签。

程序 | 描述 | commit | 备注 |
--- | --- | --- | ---
| Albumy | Albumy评论模板中的用户头像应该使用中等尺寸，即`avatar_m` | [4c6622c](https://github.com/greyli/albumy/commit/4c6622cc30377ebf2e1da64f570de71ddcc522d2) |  |
| Albumy | 图片详情页上的开启/关闭评论按钮应该使用表单实现，提交POST请求 | [4ef2898](https://github.com/greyli/albumy/commit/4ef28988586fc09a64e31b87722b83615416b1cd) | 由[Shimada666](https://github.com/Shimada666)发现 |
| CatChat | 删除用户功能时的删除按钮的class写错了，而且JavaScript中的事件函数需要监听document | [c264aac](https://github.com/greyli/catchat/commit/c264aac6fd35f527e0bd461b88fa05ab207b55f2) |  |

## 新变化提示

* 第1章：PyCharm 2018.2版本增加了对Pipenv的支持。
* 第1章：Pipenv自2018.6.25版本后在Windows中激活虚拟环境后会显示虚拟环境提示符。
* 第15章中的Flask-Share源码对应0.1.0版本。
