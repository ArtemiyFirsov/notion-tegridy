import os


class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const(%s)" % name)
        self.__dict__[name] = value


import sys
import platform

_const = _const()

if os.name == "nt":
    _const.NotionCachePath = r"D:\notion-tegridy\.notion-py"
elif os.name == "posix":
    machine = platform.machine().lower()
    if "iphone" in machine:
        _const.NotionCachePath = "/private/var/mobile/Containers/Shared/AppGroup/B776893B-6DD9-440C-874A-038C9FD788B1/File Provider Storage/Repositories/notion-tegridy/.notion-py"
    elif "ipad" in machine:
        _const.NotionCachePath = "/private/var/mobile/Containers/Shared/AppGroup/0E89090C-35CC-4B33-A31D-9A297BB590C1/File Provider Storage/Repositories/notion-tegridy/.notion-py"
    else:
        raise Exception("Unknown OS")
else:
    raise Exception("Unknown OS")

_const.ShoppingListURL = "https://www.notion.so/762a5a2cb95b48848af8752ca7336898"


sys.modules[__name__] = _const
