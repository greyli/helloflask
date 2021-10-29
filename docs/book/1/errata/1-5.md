## 第 1 版第 5 次印刷勘误

发布时间：2019/10/24


- P16倒数第一个代码块上方段落的第一句，原文为“**我们在项目根目录下分别创建两个文件**”改为“**我们在程序根目录（程序主脚本或程序包所在目录，比如helloflask/demos/hello/）下分别创建两个文件**”
- P33 图2-4前的正文最后一句中requset改为request
- P181 代码清单6-1下面的六行变量定义中的等号两边不留空格，以第一行变量定义为例，原文：
```python
MAIL_SERVER = os.getenv('MAIL_SERVER'),
```
改为：
```python
MAIL_SERVER=os.getenv('MAIL_SERVER'),
```
- P186 第二个代码块第三行中删除apikey=
该代码块下方文字删除“**使用apikey关键字**”
P187倒数第一个代码块第5行中删除apikey=
P188代码清单6-4第6行中删除apikey=
- P182代码清单6-2第一行新插入一行：
```python
# 示例程序源码做了某些调整，实际的函数名为 send_smtp_mail
```
P188代码清单6-4第一行新插入一行：
```python
# 示例程序源码做了某些调整，实际的函数名为send_api_mail
```
P191代码清单6-7第一行新插入一行：
```python
# 示例程序源码做了某些调整，实际的发信函数名为send_async_mail
```
- P237 代码清单8-9第一行新插入一行（左边无空格）：
```python
from sqlalchemy.exc import IntegerityError
```
- P250 代码清单8-23 第三行最后添加一个英文冒号
- P258 代码清单8-26 最后插入新的一行（左边无空格）：
```python
{% endblock %}
```
- P260 上方代码块最后一行中的unicode改为unidecode
- P263上面的代码块第6行中的filer改为filter
- P451倒数第二个代码块上面的正文，倒数第二行的“**我们使用资源端点支持的HTTP方法作为类方法名，它会处理对应类型的请求。**”修改为“**我们使用资源端点支持的HTTP方法名的小写形式（即get、post、delete等）作为类方法名，这些类方法会匹配处理对应类型的请求。**”
- P659代码清单16-20倒数第四行改为（缩进不变）
```python
self._obj.__dict__[name] = value
```
倒数第1行改为（缩进不变）：
```python
del self._obj.__dict__[name]
```
- P660 删除掉第一个代码块第6和第7行
