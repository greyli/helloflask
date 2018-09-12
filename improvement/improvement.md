[主页](https://github.com/greyli/helloflask)
/ [勘误](https://github.com/greyli/helloflask/blob/master/errata/errata.md)
/ [FAQ](https://github.com/greyli/helloflask/blob/master/faq/faq.md)
/ 可改进实现
/ [更新记录](https://github.com/greyli/helloflask/blob/master/CHANGES.md)
/ [示例程序](https://github.com/greyli/helloflask/blob/master/demos/)
/ [HelloFlask.com](http://helloflask.com)
/ [本书主页](http://helloflask.com/book)

# 可改进的实现

下面是《Flask Web开发实战》的可改进实现。书中的第二部分的程序编写时需要同时写作书稿，时间上比较仓促，没有深入思考程序的设计与实现。

如果你发现了书中的可改进实现，欢迎提交PR更新可改进实现文件；你也可以创建Issue指出相关问题，或是通过Email与我联系（[withlihui@gmail.com](mailto:withlihui@gmail.com)），谢谢！

这个文件的编写模式还有待确定，欢迎各种有益的探索。

## 文本描述与章节安排等

### 前言和附录中的勘误URL

GitHub上的勘误文件阅读体验不太好，而且部分地区访问较慢，我在helloflask创建了一个镜像勘误页面，可以将前言和附录中的勘误URL改为 http://helloflask.com/book/errata 。

### 介绍Git标签部分容易产生误解

在前言中介绍Git基本用法中的列出Git标签部分时，因为作为示例的helloflask并没有包含Git标签，所以这里容易产生误解，应该添加一个说明。

### 第10章开头的启动命令

在本章开头给出的初始化命令应该加入`flask translate compile`，以便生成MO文件，让程序中的语言切换生效。因为这个命令对应的内容在10.2.4，这里可以添加一句提示。

### 后记

拿到书才发现，编辑把我的后记删掉了。因为成本问题，临时妥协的解决方法是在重印时稍加修改后放到前言最后的空白处。尽管如此，还是希望有机会添加一个后记。

## 程序设计与实现

### Albumy

#### 9.4.3 写入用户权限中的角色与权限字典的设计

* 相关Issue：https://github.com/greyli/albumy/issues/1
* 贡献者：@[AngelLiang](https://github.com/AngelLiang)
* 主要描述：「代码应尽量完全表达设计者的思路」。在设计角色和权限字典时，虽然Guest和Blocked用户没有任何权限，但是应在代码中有所体现，所以此处应该添加注释：

```py
roles_permissions_map = {
    # 'Guest': [],
    # 'Blokced': [],
    'Locked': ['FOLLOW', 'COLLECT'],
    'User': ['FOLLOW', 'COLLECT', 'COMMENT' 'UPLOAD'],
    'Moderator': ['FOLLOW', 'COLLECT', 'COMMENT', 'UPLOAD', 'MODERATE'],
    'Administrator': ['FOLLOW', 'COLLECT', 'COMMENT', 'UPLOAD', 'MODERATE', 'ADMINISTER']
}
```

### bluelog

#### 虚拟数据中相关代码的优化

* 相关Issue：https://github.com/greyli/bluelog/issues/1
* 贡献者：@[AngelLiang](https://github.com/AngelLiang)
* 主要描述：「尽量使虚拟数据接近真实的数据」。虚拟数据中生成的评论时间应该晚于文章时间，评论回复时间应该晚于评论时间，并且评论和回复应关联同一篇文章。不过由于虚拟数据主要目的是展示或测试视觉效果，所以不必把太多精力放在这里。

## 排版、风格设计

### 每一部分开头配图

可以有下面的改进：

* 每一部分开头的Flask图片我曾要求编辑将其缩小放到右上角，但是电子版没有调整，结果图片太大了，大到能够看清我蹩脚处理后留下的锯齿。
* 自己画这几个图片，去掉版权声明。

### 封面配图

* 封面的图片颜色和设计图相比有些失真，需要完善。
* 图片可以再大一点。
