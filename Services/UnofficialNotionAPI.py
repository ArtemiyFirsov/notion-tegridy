import os
from Constants import constants

os.environ["NOTION_DATA_DIR"] = constants.NotionCachePath

import notion.block as block
import notion.client as clientModule
from typing import List

from Constants import constants
from Services.BaseNotionWrapper import BaseNotionAPI


class NotionAPI(BaseNotionAPI):
    def __init__(self):
        token_v2 = constants.NotionTokenV2
        self._client = clientModule.NotionClient(token_v2=token_v2)

    def add_todos(self, page_url: str, todos: List[str]):
        page = self._client.get_block(page_url)

        for arg in todos:
            previous = [i for i in page.children if i.title.lower().strip() == arg.lower().strip()]
            if len(previous) > 0:
                child = previous[0]
                child.checked = False
            else:
                child = page.children.add_new(block.TodoBlock, title=arg)
            if len(page.children) > 0 and child.id != page.children[0].id:
                child.move_to(page.children[0], "before")

    def sort_todos(self, page_url: str):
        page_url = constants.ShoppingListURL
        page = self._client.get_block(page_url)

        children_filtered = [i for i in page.children if type(i) == block.TodoBlock and i.title]
        unchecked_count = len([i for i in page.children if not i.checked])
        curr_unchecked_count = 0
        for i, child in enumerate(children_filtered):
            if curr_unchecked_count == unchecked_count:
                break
            if not child.checked and i > 0:
                child.move_to(page.children[0], "before")
                curr_unchecked_count += 1
