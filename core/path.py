import os


def getRootPath():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def getProjectAbsPath(*path):
    return os.path.join(getRootPath(), *path)


def getCachePath(*path):
    return getProjectAbsPath(".cache", *path)


def getTemplatePath(*path):
    return getProjectAbsPath("cli", "templates", *path)


def getNodeBinPath(name):
    return getProjectAbsPath("node_modules", ".bin", name)


def getPipEnvBinPath(name):
    return getProjectAbsPath("env", "bin", name)


def getCurrentAbsPath(path="."):
    if os.path.isabs(path):
        return os.path.abspath(path)
    else:
        return getCurrentAbsPath(os.path.join(os.getcwd(), path))
