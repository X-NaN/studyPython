# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    : 2022/4/11 3:28 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 
"""
import os

import pytest

if __name__ == '__main__':
    pytest.main(["-s", "./testCases/test_cmd_configs.py/", "--env=dev", "--prop=nana", "--prop=leo", '--cmdopt','--ch=java'])
    # pytest.main(["-v", "/Users/conanmu/code/github/python/studyPython/studyPytest/fixtures/test_fixture_one.py", "--env=dev"])
    # 测试hook函数 pytest_generate_tests
    # pytest.main(["-q", "./testCases/parametrize/test_parametrize.py/::test_hook_pytest_generate_tests", "--stringinput=hello", "--stringinput=123"])

# # 读取环境变量
#     caseId= os.getenv("caseId", 0)
#     print(caseId)
