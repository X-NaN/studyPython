# -*- encoding: utf-8 -*-
"""
@File    : conftest.py
@Time    : 2022/4/19 4:27 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 内嵌fixture:request，获取请求上下文
"""
import pytest


@pytest.fixture(autouse=True)
def fixture_request(request):
    print("\n======================= 内嵌fixture request start=================================")
    # 调用该fixture的module:
    print(str(request.module))
    # 调用该fixture的func
    print(request.function)
    # 调用该fixture的class
    print(request.cls)
    # 调用该fixture的路径
    print(request.fspath)
    print(request.fixturenames)
    print(request.fixturename)
    print(request.scope)
    print("\n=======================request end=================================")
