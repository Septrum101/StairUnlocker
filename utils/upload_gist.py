import json

import requests
from loguru import logger

from utils.config import config


def upload(content):
    def create():
        create_file = requests.post("https://api.github.com/gists",
                                    data=json.dumps({"files": {"stairunlocker": {"content": content}}}),
                                    headers={"Authorization": "token " + config['token'],
                                             "Accept": "application/vnd.github.v3+json"})
        if create_file.status_code == 201:
            logger.info("Writing to Gist success!\nRaw URL: " +
                        json.loads(create_file.text)['files']['stairunlocker']['raw_url'])
        else:
            logger.error(json.loads(create_file.text)['message'])
            raise Exception(json.loads(create_file.text)['message'])
        config.update({'gistURL': json.loads(create_file.text)['url']})
        config.pop("VERSION")
        with open('stairunlock_config.json', 'w', encoding='utf-8') as _:
            json.dump(config, _, indent=2, ensure_ascii=False)

    def generate_url(raw):
        raw = raw.split('/')
        raw.pop(-2)
        return "/".join(raw)

    if 'gistURL' not in config or config['gistURL'] == "":
        create()
    else:
        mod_file = requests.post(config['gistURL'],
                                 data=json.dumps({"files": {"stairunlocker": {"content": content}}}),
                                 headers={"Authorization": "token " + config['token'],
                                          "Accept": "application/vnd.github.v3+json"})
        if mod_file.status_code == 404:
            logger.error("Writing to gist fail: " + json.loads(mod_file.text)['message'])
            create()
        elif mod_file.status_code == 200:
            logger.info("Writing to gist success!\nRaw URL: " + generate_url(json.loads(mod_file.text)['files']
                                                                             ['stairunlocker']['raw_url']))
        else:
            logger.error("Writing to gist fail: " + json.loads(mod_file.text)['message'])
