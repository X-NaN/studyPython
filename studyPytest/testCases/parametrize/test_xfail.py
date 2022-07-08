# -*- encoding: utf-8 -*-
"""
@File    : test_xfail.py
@Time    : 2022/7/8 11:17 上午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: xfail用法

执行结果中：xfailed表示预期失败，实际失败, xpassed表示预期失败，实际成功
"""
import pytest


@pytest.mark.parametrize("input,expected", [("3+5", 8), ("4+2", 7), pytest.param("6*9", 1, marks=pytest.mark.xfail)])
def test_eval_xfail(input, expected):
    """
    xfail：期望失败的
    :param input:
    :param expected:
    :return:
    """
    assert eval(input) == expected


@pytest.fixture(scope='session')
def count():
    a = 1
    b = 2
    c = a + b
    return c


class TestXFail(object):
    def test_1(self, count):
        assert count == 3

    @pytest.mark.xfail(reason='断言失败')
    def test_2(self, count):
        assert count == 4

    @pytest.mark.xfail(reason='断言失败')
    def test_3(self, count):
        assert count == 3
