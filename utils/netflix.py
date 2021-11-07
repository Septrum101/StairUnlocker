import requests
from loguru import logger

from utils.config import config


def is_unlock(name, mix_port, curr_node, total_node):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/64.0.3282.119 Safari/537.36"}
        flag = 0
        if not config['fastMode']:
            # 自制剧
            r1 = requests.get("https://www.netflix.com/title/70242311", proxies={
                "http": "socks5h://127.0.0.1:%d" % mix_port,
                "https": "socks5h://127.0.0.1:%d" % mix_port
            }, timeout=5, headers=headers)
            if r1.status_code == 200:
                flag += 1
        else:
            flag += 1

        # 非自制剧
        r2 = requests.get("https://www.netflix.com/title/70143836", proxies={
            "http": "socks5h://127.0.0.1:%d" % mix_port,
            "https": "socks5h://127.0.0.1:%d" % mix_port
        }, timeout=5, headers=headers)
        if r2.status_code == 200:
            flag += 1

        # 解锁测试
        if flag == 0:
            logger.info("({}/{}) {}: None.".format(curr_node, total_node, name))
            ntype = "None"
        elif flag == 1:
            if config['fastMode']:
                logger.info("({}/{}) {}: None.".format(curr_node, total_node, name))
                ntype = "None"
            else:
                logger.info("({}/{}) {}: Only Original.".format(curr_node, total_node, name))
                ntype = "Only Original"
        else:
            logger.info("({}/{}) {}: Full Unlock.".format(curr_node, total_node, name))
            ntype = "Full Unlock"

    except Exception as e:
        logger.error('({}/{}) {}：Error. {}'.format(curr_node, total_node, name, (str(e.args[0].args[0]))))
        ntype = "Error"
    return ntype
