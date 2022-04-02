# -*- encoding: utf-8 -*-
"""
@File    : test_class.py
@Time    : 2022/4/2 5:38 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description:
1、通过class组织用例，类必须以Test开头，方法必须以test_开头，才会被识别为pytest测试类或者用例
2、每个测试用例都有一个唯一的类实例，不能共享类实例
"""


class TestDemo:
    value = 0

    def test_one(self):
        s = "this"
        assert "h" in s

    def test_two(self):
        s = "hello"
        assert hasattr(s, "check")

    def test_three(self):
        self.value = 1
        assert self.value == 1

    def test_four(self):
        assert self.value == 1
