import os
import signal
import subprocess
import sys
import time

from loguru import logger

from utils.config import config
from utils.platform_check import check_platform


class Clash(object):
    def __init__(self):
        self._process = None

    @staticmethod
    def _check_platform():
        return check_platform()

    def start_client(self):
        logger.info(f"Performing clash-core on port: {config['mixPort']}.")
        try:
            if self._process is None:
                if self._check_platform() == "Windows":
                    client = "clash-windows-amd64.exe"
                elif self._check_platform() == "Linux":
                    client = "clash-linux-amd64"
                elif self._check_platform() == "MacOS":
                    client = "clash-darwin-amd64"
                else:
                    logger.critical("Your system does not supported. Please contact developer.")
                    sys.exit(1)
                self._process = subprocess.Popen(
                    [f"./clients/clash/{client}", "-f", f"{os.getcwd()}/config.yaml"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                logger.info("Starting clash-core")
                time.sleep(3)
        except FileNotFoundError:
            logger.error("Clash Core Not Found!")
            sys.exit(1)

    def _before_stop_client(self):
        pass

    def stop_client(self):
        self._before_stop_client()
        if self._process is not None:
            if self._check_platform() == "Windows":
                self._process.terminate()
            else:
                self._process.send_signal(signal.SIGINT)
            self._process = None
            logger.info("Client terminated.")
