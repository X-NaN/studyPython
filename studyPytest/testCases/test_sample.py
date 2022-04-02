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


def fun(x):
    return x + 1


def test_answer():
    assert fun(3) == 5


pytest.main(["-s", "test_sample.py"])
