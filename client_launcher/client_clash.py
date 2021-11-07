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
        logger.info("Performing clash-core on port: {:d}.".format(config['mixPort']))
        try:
            if self._process is None:
                if self._check_platform() == "Windows":
                    self._process = subprocess.Popen(
                        ["./clients/clash/clash-windows-amd64.exe", "-f", "%s/config.yaml" % os.getcwd()],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    logger.info("Starting clash-core")
                    time.sleep(3)
                elif self._check_platform() == "Linux" or self._check_platform() == "MacOS":
                    self._process = subprocess.Popen(
                        ["./clients/clash/clash-linux-amd64", "-f", "%s/config.yaml" % os.getcwd()],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    logger.info("Starting clash-core")
                    time.sleep(3)
                else:
                    logger.critical("Your system does not supported.Please contact developer.")
                    sys.exit(1)
        except FileNotFoundError:
            logger.error("Clash Core Not Found !")
            sys.exit(1)

    def _beforeStopClient(self):
        pass

    def stop_client(self):
        self._beforeStopClient()
        if self._process is not None:
            if self._check_platform() == "Windows":
                self._process.terminate()
            else:
                self._process.send_signal(signal.SIGINT)
            self._process = None
            logger.info("Client terminated.")
