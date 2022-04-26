# -*- encoding: utf-8 -*-
"""
@File    : logging.py
@Time    : 2022/4/15 2:41 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 日志模块
一个日志器可以有多个处理器，一个处理器可以有各自的格式器和过滤器。
DEBUG < INFO < WARNING < ERROR < CRITICAL
"""
import logging
import os
import sys
import threading
from logging import handlers
from pathlib import Path

project_name = "studyPython"


class Logger(logging.Logger):
    """
    日志器
    """
    _instance_lock = threading.Lock()

    def __init__(self, project_name):
        super().__init__("log")
        self.project_name = project_name
        self.setLevel(logging.DEBUG)
        self.create_handlers()

    @classmethod
    def instance(cls, *args, **kwargs):
        with Logger._instance_lock:
            if not hasattr(Logger, "_instance"):
                Logger._instance = Logger(*args, **kwargs)
        return Logger._instance

    def __get_path(self):
        """
        获取日志路径
        :return:
        """
        if os.getenv("env"):
            # pod里的日志路径
            log_dir = "/home/docker/log"
        else:
            current_path = os.path.dirname(os.path.abspath(__file__))
            # root_path = current_path[:current_path.index("studyPython") + len("studyPython")]
            root_path = current_path[:current_path.index(self.project_name) + len(self.project_name)]
            log_dir = root_path + "/logs"
        if not Path(log_dir).exists():
            Path(log_dir).mkdir()
        return Path(log_dir)

    def __get_log_path(self, log_leve):
        """
        获取日志路径
        :param log_leve:
        :return:
        """
        log_path = self.__get_path()
        log_path_dict = {
            logging.INFO: Path(log_path).joinpath("info.log"),
            logging.WARNING: Path(log_path).joinpath("warn.log"),
            logging.ERROR: Path(log_path).joinpath("error.log")
        }
        return log_path_dict[log_leve]

    @classmethod
    def __get_log_formatter(self):
        formatter = logging.Formatter(
            "%(asctime)s|thread: %(thread)s|%(levelname)s|%(filename)s |%(funcName)s |%(lineno)d |%(message)s"
        )
        return formatter

    def create_handlers(self):
        """
        创建handler
        :return:
        """
        if len(self.handlers) < 1:
            # 控制台输出
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(self.__get_log_formatter())
            self.addHandler(console_handler)
            # TimedRotatingFileHandler按时间切割文件;
            info_file_handler = handlers.TimedRotatingFileHandler(filename=self.__get_log_path(logging.INFO),
                                                                  backupCount=500, encoding="utf-8")
            info_file_handler.setFormatter(self.__get_log_formatter())
            self.addHandler(info_file_handler)
        else:
            for handler in self.handlers:
                handler.setFormatter(self.__get_log_formatter())


logger = Logger.instance(project_name)
