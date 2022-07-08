# -*- encoding: utf-8 -*-
"""
@File    : test_fixture_class.py
@Time    : 2022/7/8 3:04 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 
"""
import pytest


@pytest.mark.usefixtures("scope_class")
class TestFixtureClassScope:

    def test_one(self):
        print("test_one was invoked")

    def test_two(self):
        print("test_two was invoked")
