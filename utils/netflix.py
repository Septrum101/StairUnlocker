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
                "http": f"socks5h://127.0.0.1:{mix_port}",
                "https": f"socks5h://127.0.0.1:{mix_port}"
            }, timeout=5, headers=headers)
            if r1.status_code == 200:
                flag += 1
        else:
            flag += 1

        # 非自制剧
        r2 = requests.get("https://www.netflix.com/title/70143836", proxies={
            "http": f"socks5h://127.0.0.1:{mix_port}",
            "https": f"socks5h://127.0.0.1:{mix_port}"
        }, timeout=5, headers=headers)
        if r2.status_code == 200:
            flag += 1

        # 解锁测试
        if flag == 0:
            logger.info(f"({curr_node}/{total_node}) {name}: None.")
            ntype = "None"
        elif flag == 1:
            if config['fastMode']:
                logger.info(f"({curr_node}/{total_node}) {name}: None.")
                ntype = "None"
            else:
                logger.info(f"({curr_node}/{total_node}) {name}: Only Original.")
                ntype = "Only Original"
        else:
            logger.info(f"({curr_node}/{total_node}) {name}: Full Unlock.")
            ntype = "Full Unlock"

    except Exception as e:
        logger.error(f"({curr_node}/{total_node}) {name}：Error. {str(e.args[0].args[0])}")
        ntype = "Error"
    return ntype
