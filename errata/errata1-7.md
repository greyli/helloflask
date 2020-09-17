## 第 1 版第 7 次印刷勘误

整理时间：2020/9/16

## 错误更正

- P115 代码块第八行中 「Field must be at least 8 characters long.」改为「Field must be between 8 and 128 characters long.」
- P126 第一个代码块第一行导入语句 `from werkzeug import secure_filename` 改为 `from werkzeug.utils import secure_filename`
- P150 第二个代码块第一行 `print(Note.query.filter_by(body='SHAVE'))` 改为 `print(Note.query.filter(Note.body=='SHAVE'))`
- P160 第一个提示段落中「……属性赋值给一个……」改为「……属性赋值为一个……」
- P165 代码清单5-14 第四行改为 `capital = db.relationship('Capital', back_populates='country', uselist=False)` 最后一行改为 `country = db.relationship('Country', back_populates='capital')`
- P177 第一段最后一行中「**kwargs字典」删掉开头的两个星号，改为「kwargs字典」

## 描述优化

- P393 代码清单9-74第5~8和第10行缩进多了四个空格，需要向左移动四个空格
- P393 倒数第二行「login_manager 对象」改为「login_manager 对象（位于 extensions.py 文件中）」
- P624 第二个代码块上方文字最后添加提示「使用下面的……Wheel 包（如果出错则需要先执行 pip install wheel 命令来安装 wheel）：」
