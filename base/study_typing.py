"""
python类型检查模块typing，python3.5以上可以使用
作用：
1、类型检查，检查函数入参和返回类型，注意并不会影响程序的运行，不会报正式的错误，只有提醒。
用法：
定义函数时，入参为paramName:"类型",返回结果为：->"返回类型"
def func(paramName:"类型")->"返回类型"

注意：在调用函数时，如果传入错误的类型，pycharm会给出提示
"""

from typing import Tuple, List, Dict


def typing_demo1(a: int, string: str, f: float, b: bool) -> Tuple[List, Tuple, Dict, bool]:
    list1 = list(range(a))
    tup = (string, string, string)
    d = {"a": f}
    bl = b
    return list1, tup, d, bl
    # return "test"


def typing_demo(a: "int", string: "str", f: "float", b: "bool") -> "Tuple[List, Tuple, Dict, bool]":
    list1 = list(range(a))
    tup = (string, string, string)
    d = {"a": f}
    bl = b
    return list1, tup, d, bl
    # return "test"


if __name__ == '__main__':
    print(typing_demo(5, "hhhh", 2.3, False))
