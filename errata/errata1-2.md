
## 临时勘误

为重印新版本暂存的勘误，未来或许会合并到 errata.md 里。

### 1-2

发布时间：预计为 2019 年初

章节 | 页码 | 位置 | 错误文字 | 正确文字 | 备注 | 发现时间 |
--- | --- | --- | --- | --- | --- | ---
| 7.3.1 | P207 | 3.7.1节中最后一段话中 | bootstrap_load_js() | bootstrap.load_js() | 笔误 | 18.11.17 |
| 7.4.3 | P213 | 最后 1 个附注段落 | bootstrap.bundle.min.css |  bootstrap.bundle.min.js | 笔误 | 18.12.5 |
| 7.5 | P213 | 最后一行代码 | `fake = Faker('zh_CN'))` |  `fake = Faker('zh_CN')` | 笔误 | 18.11.17 |
| 7.5 | P214 | 该页（节）最后 2 个代码块的最后 1 行 | | 两处均向左缩进 4 格，和上面对齐 | 排版错误 | 18.12.6 |
| 8.2.1 | P237 | 代码清单 8-8 倒数第 3 行 | | 添加注释：`# 这个方法将在 8.4.3（P273）节介绍` | 后续内容前置提示 | 18.12.6 |
| 8.3.5 | P264 | 图 8-8 上的代码块第2行 | `{{ comment.replied.author.name }}` | `{{ comment.replied.author }}` | 笔误 | 18.12.6 |
| 8.3.5 | P265 | 第1个代码块倒数第11行 | `Reply</a>` | `Reply</a></div>` | 笔误 | 18.12.6 |
| 8.3.7 | P268 | 第1行 | photo | show_post | 笔误 | 18.12.6 |
| 8.4.1 | P273 | 纸书该页第 2 个代码块，电子书 8.4.2 上面倒数第 2 个代码块。第 5、7 行 | `check_password` | `validate_password` | 笔误 | 18.12.6 |
| 8.5.3 | P278 | 代码清单8-37代码块第1行 | `from flask_login import logout_user` | `from flask_login import logout_user, login_required` | 代码错误 | 18.12.6 | 
| 8.7.1.2 |P288 | 代码清单8-42代码块倒数第2行  | `.show_post` | `blog.show_post`  | 笔误 | 18.12.6 | 
| 8.7.1.3 |P290 | 第1个代码块倒数第5行  | `.show_post` | `blog.show_post`  | 笔误 | 18.12.6 |
| 8.7.2 |P292 | 代码清单8-44代码块倒数第1行  | `.show_post` | `blog.show_post`  | 笔误 | 18.12.6 | 
| 8.7.2.2 |P294 | 代码清单8-45代码块下正文第1行  | `Ture` | `True`  | 笔误 | 18.12.6 | 
| 9.1.1 | P301 | 该页最后 1 行，电子书该节第 2 个代码块最后一行 | | 向左缩进 4 格 | 排版错误 | 18.12.6 |
| 9.1.1 | P302 | 9.1.2 标题上面的代码块 | `bluelog` | `myapp` | 笔误 | 18.12.6 |
| 9.2 | P304 | 图9-1左上角多了一个"搜索" | `搜索` | 去掉一个`搜索` | 笔误 | 18.12.10 |
| 9.2 | P310 | 代码清单9-3代码块第7行 | `url_for ('main.index')` |`url_for('main.index')`| 笔误 | 18.12.10 |
| 9.3.2.1 | P312 | 第二个代码块上正文倒数第1行 | Operations字典中 | Operations类中| 笔误 | 18.12.10 |
| 9.3.2.2 | P314 | 代码清单9-6代码块最后1行 | `url_for ('.reset_confirmation')` | `url_for ('.reset_confirm_email')`| 笔误 | 18.12.12 |
| 9.4.4 | P324 | 代码清单9-14代码块第4-5行 || 两处均向左缩进 4 格 | 排版错误  | 18.12.10 |
| 9.8.2 | P360 | 代码清单9-41代码块上访正文倒数第3行 | 实际动作是有用户做出的| 实际动作是由用户做出的| 笔误 | 18.12.10 |
| 9.8.3 | P363 | 代码清单9-45代码块倒数第6行 | `{% if collections %}` |`{% if collects %}`| 笔误 | 18.12.10 |
| 9.11.2 | P388| 最后一行 | 渲染avatar.html模板 |渲染change_avatar.html模板| 笔误 | 18.12.10 |
| 9.11.2 | P389| 第一个代码块下正文第1行 | avatar.html模板继承自settings.html模板 |change_avatar.html模板继承自settings/base.html模板| 笔误 | 18.12.10 |
| 9.11.2 | P389 | 代码清单9-71代码块第1行 | `{% extends 'user/settings.html' %}` |`{% extends 'user/settings/base.html' %}`| 笔误 | 18.12.10 |
| 9.11.6 | P397 | 代码清单9-79代码块倒数第5行 | `db.session.delete(current_user)` |`db.session.delete(current_user._get_current_object())`| 笔误 | 18.12.10 |
| 14.3.1 | P567 | 第二个代码块第2行| `token_urlsafe(16)` |  `secrets.token_urlsafe(16)` | 笔误 | 18.11.28 |
| 14.3.4 | P569 | 代码清单14-1 register_logger函数缺少app参数| `register_logging()` |  `register_logging(app)` | 笔误 | 18.11.28 |
| 14.4.7 | P584 | 倒数第2个代码块上方段落第5行| 放在/etc/supervisord.conf路径下 | 放在/etc/supervisor/conf.d路径下 | 笔误 | 18.11.28 |
