# 勘误

下面是《Flask Web开发实战》的勘误信息，按照勘误信息类别分类。

## 文本错误

* 电子书中第二章讲http安全中的注入防范里的主要防范方法的第三条的参数化查询中给出的示例代码缺少一个引号，原文为：
```
db.execute('SELECT * FROM students WHERE password=?, password)
```

## 源码错误

* 按照书中的描述以及实际的效果，Albumy评论模板中的用户头像应该使用中等尺寸，即`avatar_m`。代码位置在`albumy/albumy/templates/main/_comment.html:20`


## 可改进的实现

* 暂无

## 提示

* 第1章：PyCharm 2018.2版本增加了对Pipenv的支持。

## 笔误

* 暂无

