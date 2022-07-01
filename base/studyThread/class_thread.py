# -*- encoding: utf-8 -*-
"""
@File    : class_thread.py
@Time    : 2022/7/1 10:40 上午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 
"""
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self) -> None:
        print(self.num)


if __name__ == '__main__':
    for i in range(5):
        t = MyThread(i)
        print("#查看线程数量和进程数量总和:%s" % len(threading.enumerate()))
        t.start()
