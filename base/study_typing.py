"""
python类型检查模块typing，python3.5以上可以使用
作用：
1、类型检查提示，检查函数入参和返回类型，注意并不会影响程序的运行，不会报正式的错误，只有提醒。
用法：
定义函数时，入参为paramName:"类型",返回结果为：->"返回类型"
def func(paramName1: "类型", paramName2: "类型") -> "返回类型"

注意：在调用函数时，如果传入错误的类型，pycharm会给出提示
"""

from typing import Tuple, List, Dict

# 基本类型用法
# 变量名: 类型 = 默认值
param1: int = 10
param2: str = "test str"
param3: float = 2.34
success: bool = False

# List
# List、列表，是 list 的泛型，基本等同于 list，其后紧跟一个方括号，里面代表了构成这个列表的元素类型，如由数字构成的列表可以声明
var: List[int or float] = [1, 2.5]

# List嵌套
var1: List[List[int]] = [[1, 2], [2, 3]]


def typing_demo1(a: int, string: str, f: float, b: bool) -> Tuple[List, Tuple, Dict, bool]:
    list1 = list(range(a))
    tup = (string, string, string)
    d = {"a": f}
    bl = b
    return list1, tup, d, bl


def typing_demo(a: "int", string: "str", f: "float", b: "bool") -> "Tuple[List, Tuple, Dict, bool]":
    list1 = list(range(a))
    tup = (string, string, string)
    d = {"a": f}
    bl = b
    return list1, tup, d, bl


def typing_list(names: List[str]) -> str:
    [print(name) for name in names]
    return "typing list"


if __name__ == '__main__':
    # print(typing_demo(5, "hhhh", 2.3, False))
    typing_list(["abby", "lily"])
