# 勘误

下面是《Flask Web开发实战》的勘误信息，按照勘误信息类别分类。

## 重要提示

当前版本的Werkzeug包含一个bug：在Windows系统中使用Python2.7时，如果设置了`FLASK_ENV`环境变量，那么会导致出现`TypeError`异常。如果你使用的操作系统和Python版本相匹配，请参考下面的临时解决方案：找到项目根目录下的`.flaskenv`文件，将第二行的`FLASK_ENV`变量定义注释掉，比如：

```
# FLASK_ENV=development
```

这个问题已经在主分支修复，一旦0.14.2版本发布，我会更新所有项目的`Pipfile`和`Pipfile.lock`文件，届时你也可以使用`pipenv update werkzeug`命令对已经克隆的本地项目进行更新。

## 错误

* 暂无

## 不合理的实现

* 暂无

## 一般提示

* 第1章：PyCharm 2018.2版本增加了对Pipenv的支持。

## 笔误

* 7~11章多处提示签出Git标签的段落中，“GitHub”误写为“Github”。

