# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    : 2022/4/11 3:28 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 
"""
import pytest

if __name__ == '__main__':
    pytest.main(["-s", "./testCases/test_cmd_configs.py/", "--env=dev", "--prop=nana", "--prop=leo", '--cmdopt'])
    # pytest.main(["-v", "/Users/conanmu/code/github/python/studyPython/studyPytest/fixtures/test_fixture_one.py", "--env=dev"])
