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
    if "pyto" in sys.executable.lower():
        _const.NotionCachePath = "/private/var/mobile/Containers/Shared/AppGroup/0E89090C-35CC-4B33-A31D-9A297BB590C1/File Provider Storage/Repositories/notion-tegridy/.notion-py"
    else:
        raise Exception("Unknown OS")
else:
    raise Exception("Unknown OS")

_const.NotionTokenV2 = "098a4f3ea3d86283e123f3dd41ec2d0d0bab865032aee44dfe3a85454eb2faeb8389446453727a338cf606d9e307a2fcf91ad53c810510415703156619a193df728ed9d2580f836dd3c3b6d5a950"
_const.ShoppingListURL = "https://www.notion.so/762a5a2cb95b48848af8752ca7336898"


sys.modules[__name__] = _const
