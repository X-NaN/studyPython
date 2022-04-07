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
pooetry init

# 3、创建虚拟环境(指定python版本)
poetry env use python3

# 显示激活的虚拟环境
poetry shell

```

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


