# -*- encoding: utf-8 -*-
"""
@File    : test_cmd_configs.py
@Time    : 2022/4/15 3:26 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 
"""
import pytest

from utils.logging import logger


def test_cmd_configs(cmd_configs):
    """
    测试搜集到的命令行参数
    :param cmd_configs: 搜集的命令行参数值
    :return:
    """
    if cmd_configs["env"] == "dev":
        logger.info("开发环境，cmd_configs的值:" + str(cmd_configs["env"]))
        logger.warn("warn日志")
    elif cmd_configs["env"] == "daily":
        logger.info("日常环境，cmd_configs的值:" + str(cmd_configs["env"]))

    # logger.info("cmd_configs的值:" + str(cmd_configs1["prop"]))


if __name__ == '__main__':
    # pytest.main(["-s", "./test_cmd_configs.py/", "--env=test"])
    pytest.main(["-s", "./test_cmd_configs.py/", "--env=dev", "--prop=nana", "--prop=leo"])