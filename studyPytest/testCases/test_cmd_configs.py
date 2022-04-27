# -*- encoding: utf-8 -*-
"""
@File    : test_cmd_configs.py
@Time    : 2022/4/15 3:26 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 
"""
import json

import pytest

from utils.logging import logger


def test_cmd_configs_another(cmd_configs):
    """
    测试搜集到的命令行参数
    :param cmd_configs: 搜集的命令行参数值
    :return:
    """
    print("我是test_cmd_configs_another的print输出")


def test_cmd_configs(cmd_configs):
    """
    测试搜集到的命令行参数
    :param cmd_configs: 搜集的命令行参数值
    :return:
    """
    if cmd_configs["env"] == "dev":
        logger.info("开发环境，cmd_configs的值:%s", str(cmd_configs["env"]))
    elif cmd_configs["env"] == "daily":
        logger.info("日常环境，cmd_configs的值:%s", str(cmd_configs["env"]))
    else:
        logger.info("env为空")
    logger.info("cmd_configs的值:" + json.dumps(cmd_configs))


if __name__ == '__main__':
    # 不知为何从当前文件触发执行，用例test_cmd_configs获取到的命令行参数env为空
    pytest.main(["-s", "./test_cmd_configs.py/", "--env=dev"])
    # pytest.main(["-s", "./test_cmd_configs.py/", "--env=dev", "--prop=nana", "--prop=leo"])
