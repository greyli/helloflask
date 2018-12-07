
## 临时勘误

为重印新版本暂存的勘误，未来或许会合并到 errata.md 里。

### 1-2

发布时间：预计为 2019 年初

章节 | 页码 | 位置 | 错误文字 | 正确文字 | 备注 | 发现时间 |
--- | --- | --- | --- | --- | --- | ---
| 7.3.1 | P207 | 3.7.1节中最后一段话中 | bootstrap_load_js() | bootstrap.load_js() | 笔误 | 18.11.17 |
| 7.5 | P213 | 最后一行代码 | `fake = Faker('zh_CN'))` |  `fake = Faker('zh_CN')` | 笔误 | 18.11.17 |
| 8.2.1.3.(1) | P237 | 代码清单8-8代码块倒数第3行 | `admin.set_password('helloflask')` | `admin.set_password('helloflask')  # 参见 8.4.1章节  安全存储密码` | 笔误 |18.12.6 |
| 8.3.5 | P264 | 代码清单8-29代码块第2行 | `{{ comment.replied.author.name }}` | `{{ comment.replied.author }}` | 笔误 | 18.12.6 |
| 8.3.5 | P265 | 第1个代码块倒数第11行 | `Reply</a>` | `Reply</a></div>` | 笔误 | 18.12.6 |
| 8.3.7 | P268 | 第1行 | photo | show_post | 笔误 | 18.12.6 |
| 8.5.3 | P278 | 代码清单8-37代码块第1行 | `from flask_login import logout_user` | `from flask_login import logout_user, login_required` | 代码错误 | 18.12.6 | 
| 8.7.1.2 |P288 | 代码清单8-42代码块倒数第2行  | `.show_post` | `blog.show_post`  | 笔误 | 18.12.6 | 
| 8.7.1.3 |P290 | 第1个代码块倒数第5行  | `.show_post` | `blog.show_post`  | 笔误 | 18.12.6 |
| 8.7.2 |P292 | 代码清单8-44代码块倒数第1行  | `.show_post` | `blog.show_post`  | 笔误 | 18.12.6 | 
| 8.7.2.2 |P294 | 代码清单8-45代码块下正文第1行  | `Ture` | `True`  | 笔误 | 18.12.6 | 
| 14.3.1 | P567 | 第二个代码块第2行| `token_urlsafe(16)` |  `secrets.token_urlsafe(16)` | 笔误 | 18.11.28 |
| 14.3.4 | P569 | 代码清单14-1 register_logger函数缺少app参数| `register_logging()` |  `register_logging(app)` | 笔误 | 18.11.28 |
| 14.4.7 | P584 | 倒数第2个代码块上方段落第5行| 放在/etc/supervisord.conf路径下 | 放在/etc/supervisor/conf.d路径下 | 笔误 | 18.11.28 |
