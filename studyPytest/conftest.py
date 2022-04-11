# -*- encoding: utf-8 -*-
"""
@File    : conftest.py
@Time    : 2022/4/11 2:36 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description:单独管理一些全局的fixture
注意事项：
1、pytest默认会读取conftest.py文件里的所有fixture
2、conftest.py文件名固定；
3、conftest.py只对同一个package下的所有测试用例有效；
4、不同目录可以有自己的conftest.py文件，一个项目可以有多个conftest.py
5、不需要手工import conftest.py文件，pytest会自动查找；
6、最顶层的conftest.py一般写全局的fixture
"""
import json

import pytest

from utils.logger import Logger

logger = Logger.instance()


def pytest_addoption(parser):
    """
    注册用户自定义命令行参数，方便用户将数据传递给pytest.
    :param parser:
    :return:
    """
    logger.info("pytest_addoption")
    # action="store"时，defualt可以为任意类型值
    parser.addoption("--env", action="store", default='', help="外部传入环境")
    parser.addoption("--prop", action="append", default=[], help="外部传入环境")
    pass


@pytest.fixture(scope="session")
def cmd_configs(request):
    logger.info("cmd_configs")
    cmd_configs = {}
    cmd_configs["env"] = request.config.getoption("--env")

    return cmd_configs


@pytest.fixture(scope="session")
def cmd_configs1(pytestconfig):
    logger.info("cmd_configs")
    cmd_configs = {}
    cmd_configs["prop"] = pytestconfig.getoption("--prop")

    return cmd_configs


@pytest.fixture()
def configs(cmd_configs):
    logger.info('--cmd_configs的值：' + json.dumps(cmd_configs))
