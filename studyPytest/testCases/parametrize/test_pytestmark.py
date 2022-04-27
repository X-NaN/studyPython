# -*- encoding: utf-8 -*-
"""
@File    : test_pytestmark.py
@Time    : 2022/4/27 4:24 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 通过pytestmark, 使module中所有测试函数/测试方法参数化
"""

import pytest

pytestmark = pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])


class TestClass:
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected
