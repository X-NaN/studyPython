# -*- encoding: utf-8 -*-
"""
@File    : test_fixture_two.py
@Time    : 2022/4/19 11:35 上午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description:
影响fixture的执行顺序的三个因素：scope，fixture依赖，autouse。
"""
import pytest


@pytest.fixture
def order():
    print("运行order")
    return []


@pytest.fixture
def c2(order):
    print("运行c2")


@pytest.fixture(autouse=True)
def c1(order):
    """
    autouse=True时，fixture会自动运行，并且其依赖的fixture也会自动变为autouse=True
    :param order:
    :return:
    """
    print("运行c1")
    return order.append("c1")


def test_order(c1):
    print("运行test_order")
