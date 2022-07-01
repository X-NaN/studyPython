# -*- encoding: utf-8 -*-
"""
@File    : func_thread.py
@Time    : 2022/7/1 10:35 上午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 面向过程多线程
"""
import threading
import time


def fun_1(i):
    print("开始执行")
    time.sleep(1)
    print("执行完成")


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=fun_1, args=(i,))
        print("#查看线程数量和进程数量总和:%s" % len(threading.enumerate()))
        t.start()
