[主页](https://github.com/greyli/helloflask)
/ 勘误
/ [FAQ](https://github.com/greyli/helloflask/blob/master/faq/faq.md)
/ [可改进实现](https://github.com/greyli/helloflask/blob/master/improvement/improvement.md)
/ [示例程序](https://github.com/greyli/helloflask/blob/master/demos/)
/ [HelloFlask.com](http://helloflask.com)
/ [本书主页](http://helloflask.com/book)

# 勘误

下面是《Flask Web开发实战》的勘误信息。

如果你发现了书中的错误，欢迎提交PR更新勘误文件；你也可以创建Issue指出相关错误，或是通过Email与我联系（[withlihui@gmail.com](mailto:withlihui@gmail.com)），谢谢！

创建PR时，请参考下列要求：

* 勘误需要按照章节顺序排列，全局错误放到最上面。
* 每一列的内容说明参考第一行。

错误分类说明：

* 笔误：错别字（包括中文和英文），也可以细分为拼写错误、大小写错误，同时包括代码中漏掉某个符号之类的错误
* 错误：描述错误、代码错误
* 审校错误：编辑后期修改和审校中引入的错误
* 排版错误：排版人员引入的错误

*因为电子书因为尺寸不同，会产生不同的页数，这里的勘误页码为纸书页码，电子书可以根据章节和位置来定位错误内容。另外，因为纸书还未发售，页数暂时为空。*


## 纸书第一版第一次印刷

发布时间：2018/9/1

章节 | 页码 | 位置 | 错误文字 | 正确文字 | 备注 |
--- | --- | --- | --- | --- | ---
| 所在章节，比如1.3.2 | 纸书页数 | 所在位置，比如第X行 | 错误的文字内容 | 修改正确的文字内容 | 额外的备注信息，比如错误类别，或是你的牢骚 |
| 全局 | - | -  | 单击 | 点击 | 审校错误。多处。编辑称这个修改是出版社的规范要求，我觉得有些莫名其妙 |
| 全局 | - | -  |  | 代码块中的英文单词换行被截断时错误的添加的连接线 | 排版错误。多处，比如9.4.1第2个代码块、9.5.2代码清单9-16等 |
| 全局 | - | -  | Github | GitHub | 大小写错误。多处 |
| 前言 | - | 本书主要特点中的第2点 | 第一部分的2~6章 | 第一部分的1~6章 | 审校错误 |
| 前言 | - | 本书主要特点中的第3点 | Pyhton | Python | 拼写错误 |
| 前言 | - | 本书主要特点中的第3点 | Boostrap | Bootstrap | 审校错误 |
| 1.2 | - | 代码清单1-1下的提示文字 | 命令为 | 命名为 | 笔误 |
| 1.2.2.2 | - | 第1个附注文字下第2行 | http://helloflask.com/hello/Grey | http://helloflask.com/greet/Grey | 笔误 |
| 1.3.3 | - | 第1行 | Enviroment  | Environment | 拼写错误 |
| 1.7 | - | 第2个代码块下第1行 | `url_for('say_hello', name='Jack')` | `url_for('greet', name='Jack')` | 笔误 |
| 2.3.2 | - | HTML小节的最后1行 | HTTP | HTML | 笔误 |
| 2.3.2 | - | 第三个代码块 | `{'Location', 'http://www.example.com'}` | `{'Location': 'http://www.example.com'}` | 笔误。返回值中字典里的符号出错 |
| 2.5.4.1 | - | 第3个代码块 | `db.execute('SELECT * FROM students WHERE password=?', password)` | `db.execute('SELECT * FROM students WHERE password=?, password)` | 笔误。字符串漏写右侧关闭引号 |
| 3.3.2 | - | 第2段文字中 | _macors.html | _macros.html | 笔误 |
| 4.3.1 | - | 第1个代码块后第1行 | 3000 | 2000 | 笔误，不同的浏览器对于URL有不同的长度限制，此处的长度为“最佳实践” |
| 5.4.1.1 | - | 第1个代码块第3行 | `'DON'T BELIEVE……'` | `'DON\'T BELIEVE……'` | 代码错误，字符串漏掉了转义符号 |
| 10.3.1.4 | - | 忘记了，待确定 | RSET | REST | 笔误 |
| 10.3.3.5 | - | 最后1行 | flask-restless | Flask-Restless | 大小写错误 |
| 11.4.3.5 | - | 代码清单11-11中多处 | `get['XXX']` | `get('XXX')` | 审校错误 |
| 11.5.1 | - | 代码清单11-13第5行 | `position === 0&& socket.nsp` | `position === 0 && socket.nsp` | 审校错误。空格缺失 |
| 15.7.3 | - | 最后1个代码块的第2行 | `git push origm` | `git push origin` | 审校错误。另外，这一行下面的Github应为GitHub |


关于URL长度限制的详情可以参考[WWW FAQs: What is the maximum length of a URL?](https://www.boutell.com/newfaq/misc/urllength.html)。

## 电子书

此处列出电子书特有的错误，多为排版错误，其他勘误请参考上面的表格。

发布时间：2018/8/24

章节 | 页码 | 位置 | 错误文字 | 正确文字 | 备注 |
--- | --- | --- | --- | --- | ---
| 全局 | - | -  | （） | () | 排版错误。所有半角括号被改为全角括号 |
| 全局 | - | -  | `foo --bar` | `foo--bar` | 排版错误。多处。比如`flask --help`被错误写为`flask--help` |
| 1.1.2 | - | 第1个代码块 |  | 排版错误。命令输出缺失内容`flask-1.0.2 itsdangerous-0.24` | 内容缺失 |
| 第5章 | - | - | `flaskinitdb` | `flask initdb` | 排版错误。命令间的空格缺失 |

## 源码错误

* 按照书中的描述以及实际的效果，Albumy评论模板中的用户头像应该使用中等尺寸，即`avatar_m`。代码位置在`albumy/albumy/templates/main/_comment.html:20`

## 可改进的实现

* 每一部分开头的Flask图片我曾要求编辑将其缩小放到右上角，但是电子版没有调整，结果图片太大了，大到能够看清我蹩脚处理后留下的锯齿。

## 新变化提示

* 第1章：PyCharm 2018.2版本增加了对Pipenv的支持。
