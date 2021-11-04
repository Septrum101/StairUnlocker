import json
import os
import shutil

__version__ = "1.00"

config = {"VERSION": __version__}

LOADED = False

if not LOADED:
    if os.path.exists("./stairunlock_config.json"):
        if os.path.isdir("./stairunlock_config.json"):
            shutil.rmtree("./stairunlock_config.json")
            if not os.path.exists("./stairunlock_config.example.json"):
                raise FileNotFoundError(
                    "Default configuration file not found, please download from the official repo and try again.")
            shutil.copy("./stairunlock_config.example.json", "stairunlock_config.json")
    else:
        if not os.path.exists("./stairunlock_config.example.json"):
            raise FileNotFoundError(
                "Default configuration file not found, please download from the official repo and try again.")
        shutil.copy("./stairunlock_config.example.json", "stairunlock_config.json")

    with open("./stairunlock_config.json", "r", encoding="utf-8") as f:
        try:
            file_config = json.load(f)
            config.update(file_config)
        finally:
            pass
    LOADED = True
