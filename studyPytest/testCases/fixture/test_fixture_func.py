# -*- encoding: utf-8 -*-
"""
@File    : test_fixture_func.py
@Time    : 2022/7/8 3:00 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: fixture基本用法，yield用法
"""
import pytest


@pytest.fixture()
def db():
    print('Connection successful')
    # yield之前的代码在测试用例之前执行
    yield
    # yield之后的代码在测试用例之后执行
    print('Connection closed')


def search_user(user_id):
    d = {
        '001': 'xiaoming'
    }
    return d[user_id]


def test_search(db):
    assert search_user('001') == 'xiaoming'


def test_fixture_scope_func(login):
    assert login == "scope_function"
