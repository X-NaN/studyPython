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


# 类中所有方法参数化
@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:

    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected
