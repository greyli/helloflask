## 第 1 版第 3 次印刷勘误

发布时间：2019/4/1

#### 重要勘误

##### 2019/4/23
位置 | 错误 | 正确 | 备注/时间 |
--- | --- | --- | ---
| 5.2 P141 第一个SQL代码块第三行 | | 去除末尾的**,**逗号 | 标点错误 19.03.12 |
| P170 附注段落最后一句 | | 你可以在命令行中输入flask db --help 查看 db 命令所有可用的子命令和说明。| 19.4.23 |
| 5.7.1 P173 上方代码块第3行 | `relationship('Comment', cascade='save-update, merge, delete')` | `db.relationship('Comment', back_populates='post', cascade='save-update, merge, delete')` | 笔误 19.03.15 |
| 5.7.1 P173 上方代码块第3行 | `relationship('Comment', cascade='all')` | `db.relationship('Comment', back_populates='post', cascade='all')` | 笔误 19.03.15 |
| 5.7.1 P174 倒数第2个代码块第3行 | `relationship('Comment', cascade='all, delete-orphan')` | `db.relationship('Comment', back_populates='post', cascade='all, delete-orphan')` | 笔误 19.03.15 |
| 第10章 P451 | `class Item(MethodView)` | `class ItemAPI(MethodView)` | 19.4.23 |
| 第五章 P167 图5-8下第二段最后一句 | 设为关联表名称 | 设为关联表对象或是字符串形式的关联表名称 | 19.4.23 |
| P255 下面代码块第 10 行 | 去掉中部的 `class="next ` |
| P269 | 去掉页面中部的提示段落 |
| P644 第一个代码块最后一行 | `name` | `name.encode()` | 19.4.23 |

#### 不重要勘误

##### 2019/4/23
位置 | 错误 | 正确 | 备注/时间 |
--- | --- | --- | ---
| 前言最后一页 | | 致谢段落最后一段需要添加独立的标题“关于彩蛋” | 出版社工作疏忽 |
| 5.1.2.1 P140 记录的文档表示的第四行 | `sex: "Male"` | `sex: "Male",` | 标点缺失 19.03.12 |
| 5.5.2 P158 代码清单 5-10 第四行第一个参数 | `db.String(70)` | `db.String(20)` | 与源码不符 19.03.13 |
| 5.5.2.4 P162 代码清单5-11第3行 | `db.String(70)` | `db.String(64)` | 与源码不符 19.03.15 |
| 5.7.1 P172 下方代码块第三行 | 与源码不符 | 去掉`, unique=True`约束 | 与源码不符 19.03.15 |
| 5.3.3 P146 代码清单5-3下方正文 | flask inintdb | flask initdb | 笔误 19.03.12 |
| 2.2.3.3 P36 中部代码块最后一行 | 多出源码中没有的`<p>`标签 | 去除`<p>`标签 | 与源码不符 19.03.07 |
| 5.5.5 P167 图 5-8 中 student 和 association 表之间的箭头 | 两张表的 id 不对应 | | 错误 19.03.15 |
| 4.4.7 P134 代码清单4-23最后两行 | 两行间的行距过大 | | 排版错误 19.03.12 |
| 5.5.2 P160-P161 正文、提示段落中共四处 | Aritcle / aritcles | Article / articles | 笔误 19.03.13 |
| 5.7.1.1 P173 中部代码块 | `comment1 =Comment()`/`comment2 =Comment()` | = 等号右边增加一个空格 | 19.03.15 |
| 6.3.2 P190 第一段正文 | HMTL | HTML | 笔误 19.03.17 |
| 6.2.3.3 P187下方代码块 P188 代码清单6-4 | `os.environ.get()` | `os.getenv()` | 19.03.17 |
| 6.2.3.3 P188 代码清单6-4 | 整段代码和源码有很多不同 | 见源码 | 19.03.17 |
| 6 P182-P191 全章节多处 | 代码清单中发送邮件的函数名与源码不一致 | 见源码 | 19.03.17 |
| 540 注释优化 | | 「定位输入按钮」改为「定位输入框」，按下按钮改为「按下回车键」| 19.4.23 |
| P453 正文第二行 | 因为 API 的无状态特性，我们不能再使用 Flask-Login 实现认证功能 | 因为客户端不一定是浏览器，我们一般不会使用 Flask-Login 实现认证功能 |
| P552 表 13-2 下面段落 | 第二句话结尾分号前追加括号文字“（可以使用 CACHE_DIR 配置变量指定缓存文件存储目录）” |

拼写错误，全书多处：Crtl 改为 Ctrl，下面是已知的错误位置：
* P139 注意段落