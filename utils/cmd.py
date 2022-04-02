# -*- encoding: utf-8 -*-
"""
@File    : cmd.py
@Time    : 2022/4/2 6:14 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 
"""
import subprocess

from utils.logger import Logger

log = Logger.instance()


def exe_cmd(cmd: str):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in p.stdout.readline():
        print(line)
        log.info(line)
    retval = p.wait()
    return retval


if __name__ == '__main__':
    exe_cmd("pytest -q test_class.py")
