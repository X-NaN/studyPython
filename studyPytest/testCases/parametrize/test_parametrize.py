# -*- encoding: utf-8 -*-
"""
@File    : test_parametrize.py
@Time    : 2022/4/27 4:12 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 数据驱动-参数化
"""
import pytest


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("input,expected", [("3+5", 8), ("4+2", 6), pytest.param("6*9", 11, marks=pytest.mark.xfail)])
def test_eval_xfail(input, expected):
    """
    xfail：期望失败的
    :param input:
    :param expected:
    :return:
    """
    assert eval(input) == expected


# 类中所有方法参数化
@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:

    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected
