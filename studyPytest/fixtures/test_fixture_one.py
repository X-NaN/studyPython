# -*- encoding: utf-8 -*-
"""
@File    : test_fixture_one.py
@Time    : 2022/4/11 10:59 上午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description:fixture
参数scope
参数autouse=Tue，表明次fixture会在给定的scope范围内自动执行，且不需要在测试方法中进行引用

yield作用以及和return区别：
yield在fixture中起到了唤起teardown的作用，同时也可以和return一样返回值。
区别是：
return执行完成，该函数终止；yield在返回结束后，后续的代码仍可执行.
如果想要用到fixture函数中的yield的返回值，则在测试方法的参数中一定要引用对应的fixture函数，所以，一般自动执行的fixture函数是没有返回值的。

"""
import json

import pytest
from utils.logger import Logger

logger = Logger.instance()


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self.__cube_fruit()

    def __cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


@pytest.fixture()
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    fruit_salad = FruitSalad(*fruit_bowl)
    assert all(fruit.cube for fruit in fruit_salad.fruit)


def test_cmd_configs(cmd_configs):
    """
    测试搜集到的命令行参数
    :param cmd_configs: 搜集的命令行参数值
    :return:
    """
    if cmd_configs["env"] == "dev":
        logger.info("开发环境，cmd_configs的值:" + str(cmd_configs["env"]))
    elif cmd_configs["env"] == "daily":
        logger.info("日常环境，cmd_configs的值:" + str(cmd_configs["env"]))

    # logger.info("cmd_configs的值:" + str(cmd_configs1["prop"]))


if __name__ == '__main__':
    # pytest.main(["-s", "./test_fixture_one.py/", "--env=test"])
    pytest.main(["-s", "./test_fixture_one.py/", "--env=dev", "--prop=nana", "--prop=leo"])
