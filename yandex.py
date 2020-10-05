import os

os.environ["NOTION_DATA_DIR"] = os.path.join("/tmp", ".notion-py")

from handlers.yandex_alice.shop_list_handler.handler import handler as ShopListHandler