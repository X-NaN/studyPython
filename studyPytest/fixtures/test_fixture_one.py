# -*- encoding: utf-8 -*-
"""
@File    : test_fixture_one.py
@Time    : 2022/4/11 10:59 上午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 
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
    logger.info("cmd_configs的值:" + cmd_configs["env"])
    print("cmd_configs的值:" + cmd_configs["env"])
