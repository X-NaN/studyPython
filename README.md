# 0、项目结构
* base--基础学习
* requirements.txt--包版本管理
* data--各类数据
* studyPytest--pytest学习代码
* util--各类工具类

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


