# -*- encoding: utf-8 -*-
"""
@File    : test_sample.py
@Time    : 2022/3/31 6:24 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: test
"""
import pytest


def add_one(x):
    return x + 1


def exception_function():
    raise SystemExit(1)


def test_answer():
    assert add_one(3) == 4


def test_answer2():
    assert add_one(3) == 5


def test_exception():
    with pytest.raises(SystemExit):
        exception_function()


def answer_test():
    """
    该方法不会被识别为pytest用例，必须以test_开头的函数才会被收集执行
    :return:
    """
    assert add_one(3) == 5


pytest.main(["-s", "test_sample.py"])
