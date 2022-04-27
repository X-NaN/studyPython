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
from utils.logging import logger


def pytest_addoption(parser):
    """
    注册用户自定义命令行参数，方便用户将数据传递给pytest.
    :param parser:
    :return:
    """
    logger.info("pytest_addoption函数")
    # action="store"时，defualt可以为任意类型值
    parser.addoption("--env", action="store", default='', help="外部传入环境")
    parser.addoption("--prop", action="append", default=[], help="外部传入prop")
    parser.addoption("--cmdopt", action="store_const",
                     default='custom',
                     const='test',
                     help="将命令行参数 ’--cmdopt' 添加到 pytest 配置中")
    parser.addoption("--ch", action="store",
                     default='test',
                     choices=['python', 'java', 'c++'],
                     help="将命令行参数 ’--ch' 添加到 pytest 配置中")
    pass


def pytest_configure(config):
    logger.info("pytest_configure函数执行")


def pytest_collection_modifyitems(session: "pytest.Session", config: "Config", items
                                  ) -> None:
    logger.info("pytest_collection_modifyitems函数执行")


@pytest.fixture(scope="session")
def cmd_configs(request):
    logger.info("cmd_configs函数")
    cmd_configs = {}
    cmd_configs["env"] = request.config.getoption("--env")
    cmd_configs["prop"] = request.config.getoption("--prop")
    cmd_configs["cmdopt"] = request.config.getoption("--cmdopt")
    cmd_configs["ch"] = request.config.getoption("--ch")

    return cmd_configs
