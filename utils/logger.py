import sys
import os
import threading
import logging
from pathlib import Path
from logging import handlers


class Logger(logging.Logger):
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        super().__init__("nana")
        self.config_format()

    @classmethod
    def instance(cls, *args, **kwargs):
        with Logger._instance_lock:
            if not hasattr(Logger, "_instance"):
                Logger._instance = Logger(*args, **kwargs)
        return Logger._instance

    def config_format(self):
        if len(self.handlers) < 1:
            self.setLevel(logging.DEBUG)
            console = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                "[%(asctime)s]  [%(levelname)s]  [%(filename)s: %(lineno)d]  %(message)s"
            )
            console.setFormatter(formatter)
            self.addHandler(console)
            if os.getenv("env"):
                pod_log_dir = "/home/docker/log"
            else:
                current_path = os.path.dirname(os.path.abspath(__file__))
                root_path = current_path[:current_path.index("studyPython") + len("studyPython")]
                pod_log_dir = root_path + "/logs"
            if not Path(pod_log_dir).exists():
                Path(pod_log_dir).mkdir()
            file_name = Path(pod_log_dir).joinpath("info.log")
            file_config = handlers.TimedRotatingFileHandler(
                filename=file_name, backupCount=500, encoding="utf-8"
            )
            file_config.setFormatter(formatter)
            self.addHandler(file_config)
            return
        for h in self.handlers:
            self.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                "[%(asctime)s]  [%(levelname)s]  [%(filename)s: %(lineno)d]  %(message)s"
            )
            h.setFormatter(formatter)
