## 第 1 版第 4 次印刷勘误

发布时间：2019/7/1

- P6 最后的提示段落改为注意段落，内容改为
> 注意 使用 Pipenv 会更方便，但你需要注意它的“自动更新锁定依赖”的设定。另外，使用 Pipenv 来管理虚拟环境和依赖并不是必须的，事实上，使用 virtualenv/venv 和 pip 来手动管理虚拟环境和依赖是更稳定的方式，阅读 http://greyli.com/back-to-virtualenv-venv-and-pip/ 了解详细内容。使用 virtualenv/venv+pip 时，手动激活虚拟环境后，只需将本书安装命令中的 pipenv 替换为 pip 即可。
- P9 步骤2第1行最后 选择我们的 改为 选择我们在前言「使用示例程序」部分克隆仓库对应的文件夹
- P11 1.2 小节第一段 本书的第一部分每一章对应一个示例程序 后面添加 （请先阅读前言「使用示例程序」部分把示例程序克隆到本地）
- P109 第一个代码块第一行 >>> form = LoginForm() 修改为（#号前后各一个空格）：
```python
>>> form = LoginForm() # 注意，这里使用的 LoginForm 是 4.2.1 小节开头的表单类定义
```
- P127 提示段落下面的正文第2 行 重定向到 show_images 视图 改为重定向到 show_images 视图（具体视图和模板定义见示例程序源码）
- P143 表 5-2 在标题行下面新插入两行
模式 dialect+driver://username:password@host:port/databasename （数据库接口/driver部分省略会使用默认选项）
Microsoft SQL Server mssql://username:password@host:port/datebasename
- P144 表 5-3 左侧标题行 字段 改为 字段类型
- P171 第 3 小节代码块第一行删除开头的 >>> 和紧跟着的一个空格 
- P185 上面的代码块最后一行插入新的一行：
```python
MAIL_DEFAULT_SENDER = ('Grey Li', 'grey@example.com')
```
- P208 第 1 个代码块第 6 行 `render_form(form),action=request.full_path` 修改为 `render_form(form, action=request.full_path)`
- P213 第 1 个附注段落 `bootstrap.bundle.min.css` 改为 `bootstrap.bundle.min.js`
- P235 下方代码块第三行中的 backref 改成 back_populates
- P585 最后两行中的 bluelog 分别和 stop、start 调换位置，修改后：
```
$ sudo supervisorctl stop bluelog
$ sudo supervisorctl start bluelog
```
- P684 上面的列表第四行替换为下面文字：
HelloFlask 仓库：https://github.com/greyli/helloflask/issues
