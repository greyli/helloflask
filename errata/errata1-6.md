## 第 1 版第 6 次印刷勘误

整理时间：2020/6/30

从这次开始，把描述优化的内容也一并记录在勘误文件里。

## 错误更正

- P32 get_data() 方法所在行（第九行）：
  - 左侧参数 parse_from_data 改为 parse_form_data
- P104 更新三个 Python 包名称后括号内的版本号：
  - 2.2 改为 2.2.1
  - 0.14.2 改为 0.14.3
  - 0.4.0 改为 0.4.3
- P214 正文第一段最后的“fake”修改为“forge”
- P237 代码清单 8-9 导入语句第一行 `from sqlal chemy.exc import IntegerityError` 修改为 `from sqlalchemy.exc import IntegrityError`
  - `sqlal chemy.exc` 删除中间多出的空格
  - `IntegerityError` 删除多余的第二个 e
- P566 提示段落第一行中“post-revive”改为“post-receive”
- P624 倒数第二段结尾中的“吸入”改为“写入”

## 描述优化

- 前言第一段中：
  - “根据 2018 年”改为“根据 2018 和 2019 年”
  - “截至 2019 年 4 月”改为“截至 2020 年 6 月”
  - “42000”改为“51000”
  - “2000”改为“2300”
- P7 第一个提示段落整段修改为：
  - Pipenv 会自动管理虚拟环境，使用 pipenv install 命令会自动把包安装到虚拟环境内。如果你使用 venv 或 virtualenv 手动管理虚拟环境，上面的命令等价于激活虚拟环境后再执行 pip install flask。不论使用哪一种工具安装 Python 包，笔者都建议将 PyPI 源地址设置为国内的 PyPI 镜像服务器，这样可以提高下载 Python 包文件的速度，具体方法可以参考 [http://greyli.com/set-pypi-mirror/](https://greyli.com/set-pypi-mirror/)。
- P32 data 属性所在行（第四行）右侧说明最后追加“，内部调用 get_data() 方法，同时将 parse_form_data 参数设为 True，建议优先使用 get_data 方法”
- P32 get_data() 方法所在行（第九行）：
  - “获取请求中的数据，”修改为“返回字符串格式的请求数据。cache 设置是否缓存解析后的数据以供后续调用。因为解析表单数据的函数不缓存解析结果，如果解析过表单或是显式的将 parse_form_data 设为 True，那么这里会返回空值”
- P118 删除下方的整个注意段落。如果出于排版考虑没法整个删除，那就删除第二句话。
- P304 注意段落最后追加一句“未签出前的版本即对应下一节给出的文件目录结构。”
- P246 第四行中“实现了”改为“基于 Bootstrap 实现了”
