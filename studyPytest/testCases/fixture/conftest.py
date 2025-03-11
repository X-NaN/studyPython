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


@pytest.fixture()
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


@pytest.fixture(scope="function")
def login():
    """
    函数级，每个测试函数都会执行一次该fixture
    :return:
    """
    return "我是scope_function"
    pass


@pytest.fixture(scope="class")
def scope_class():
    """
    类级别，每个测试类执行一次，其中的所有的方法都可以使用
    :return:
    """
    print("我是scope_class")
    return "scope_class"
    pass


@pytest.fixture(scope="module")
def scope_module():
    """
    module级别，每个模块执行一次，其中所有的函数和方法都可以使用
    :return:
    """
    pass


@pytest.fixture(scope="session")
def scope_session():
    """
    会话级，一次测试只执行一次，所有被找到的函数和方法都可用
    :return:
    """
    pass
