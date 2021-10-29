## 第 1 版第 10 次印刷勘误

整理时间：2021/5/11


## 勘误贡献者

- @Yuxiaoy1 Yuxiaoy1 https://github.com/Yuxiaoy1
- @Skylor-Tang Skylor-Tang https://github.com/Skylor-Tang
- @panla panla https://github.com/panla


## 错误更正

- P24 代码清单 1-4 第一行插入导入语句：

```python
import click

```
- P116 注意段落第一句「因为 WTForms 会」改为「因为 Flask-WTF 会」
- P150 第二个代码块第一行 `print(Note.query.filter(body='SHAVE'))` 改为 `print(Note.query.filter(Note.body=='SHAVE'))`
- P164 第一个代码块最后一行中的「`relationship`」改为「`db.relationship`」
- P333 第一句「可以在 `create()` 方法中使用 `redirect_url` 参数指定上传后跳转的端点或 URL」改为「可以在 `config()` 方法中使用 `redirect_url` 参数指定上传后跳转的 URL」。
- P380 第二个代码块的第一行：

```python
from albumy.notifications import push_new_follower_notifications
```

改为：

```python
from albumy.notifications import push_follow_notifications
```

- P545: 第二个代码块上方的「bluelog 程序包」改为「sayhello 程序包」
- P595 倒数第二个代码块第一行：

```
$ heroku login
```

改为：

```
$ heroku login -i
```

同时该代码块下面的附注段落前面插入一句话：「不添加 `-i` 选项将会打开浏览器进行登陆操作。」
- P610 代码清单 15-3 第三行：

```python
def init_app(app):
```

改为：

```python
def init_app(self, app):
```

- P613 代码清单 15-7 第七行及其下面四行和源码不一致：

```python
platform = request.user_agent.platform
mobile_pattern = re.compile('android|fennec|iemobile|iphone|opera (?:mini|mobi)')
m = re.match(mobile_pattern, platform)
if m is not None:
    return ''
```

改为：

```python
platform = request.user_agent.platform
if platform is not None:
    mobile_pattern = re.compile('android|fennec|iemobile|iphone|opera (?:mini|mobi)')
    m = re.match(mobile_pattern, platform)
    if m is not None:
        return ''
```


## 描述优化

- 前言第一句「根据 2018 和 2019 年」改为「根据 2018、2019 和 2020 年」
- P16 页中代码块下面文字第一句括号中的句子「（程序主脚本或程序包所有目录，比如 `helloflask/demas/hello/`）」改为「（程序主脚本或程序包同级目录，比如 `helloflask/demos/hello/` 或本书第二部分的程序 `sayhello/` 等）」。第二行开头「建两个文件：`.env` 和 `.flaskenv`」改为「建两个文件：`.env` 和 `.flaskenv`（可以使用编辑器创建，注意不要漏掉文件名开头的点）」
- P167 代码块上方段落最后一句话「而在 `Teacher` 类上的 `students` 集合属性会返回……」改为 「而在 `Teacher` 类上我们可以创建一个 `students` 集合属性来返回……」
- P196 表 7-1 删除第一行：sayhello/ | 程序包
- P198 页中代码上方最后一句话追加「（如果还没有创建 `.flaskenv` 文件，可以使用编辑器在项目根目录，即 sayhello 程序包的同级目录创建该文件，注意不要漏掉文件名开头的点）」
