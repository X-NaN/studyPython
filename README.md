# 0、项目结构
* base--基础学习
* requirements.txt--包版本管理
* data--各类数据
* studyPytest--pytest学习代码
* util--各类工具类

## 0.1 poetry
使用poetry管理依赖和打包,官网地址：https://python-poetry.org/docs/

```shell
# 1、安装poetry
pip install --user poetry

# 创建项目,创建脚手架（不推荐）
poetry new 

# 2、已有项目使用poetry, 该命令会创建一个pyproject.toml文件,提示输入，不确定的可以直接跳过
poetry init

# 3、创建虚拟环境(指定python版本)
poetry env use python3

# 显示激活的虚拟环境
poetry shell

```

### 0.1.1 常用命令
参考文档：https://zhuanlan.zhihu.com/p/445952026


|命令|功能|示例｜
|----|----|----|
|new|创建项目脚手架，包含基本 的结构和pyproject.toml|poetry new <项目名xx>|
|init|基于已有的项目创建pyproject.toml，支持命令行输入基本信息|poetry init|
|install|安装依赖库|poetry install|
|update|更新依赖库||
|add|添加依赖库|poetry add <dependency_name>|
|remove|移除依赖库||
|show|显示依赖库信息，支持显示树形依赖链||
|build|支持构建tar.gz或者wheel包||
|push|发布到PyPI||

# 1、Pytest
## 1.1 安装pytest
```shell
# 安装pytest
pip install -U pytest

# 检查pytest版本
pytest --version
```
## 1.2 编写并运行用例
```python
"""
官方文档：https://docs.pytest.org/en/latest/getting-started.html
test_sample.py文件
"""
import pytest


def fun(x):
    return x + 1


def test_answer():
    assert fun(3) == 5


pytest.main(["-s", "test_sample.py"])

```
```shell
# 第一种
# 进入项目根目录下
cd xxx
# 执行pytest
pytest

#第二种:pytest.main(["-s", "test_sample.py"])
```


