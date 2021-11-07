import platform


def check_platform():
    tmp = platform.platform()
    if "Windows" in tmp:
        return "Windows"
    elif "Linux" in tmp:
        return "Linux"
    elif "Darwin" in tmp or "mac" in tmp:
        return "MacOS"
    else:
        return "Unknown"
