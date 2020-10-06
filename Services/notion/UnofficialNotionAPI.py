import os

from Constants import constants

os.environ["NOTION_DATA_DIR"] = constants.NotionCachePath

import notion.block as block
import notion.client as clientModule
from typing import List

from Constants import constants
from Services.notion.BaseNotionWrapper import BaseNotionAPI


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
        page = self._client.get_block(page_url)

        children_filtered = {i: v for i, v in enumerate(page.children) if type(v) == block.TodoBlock and v.title and not v.checked}

        for ind, child in children_filtered.items():
            if child.id == page.children[0].id:
                continue

            if not page.children[ind-1].checked:
                continue

            if not child.checked:
                child.move_to(page.children[0], "before")

    def delete_todos_duplicates(self, page_url: str):
        page = self._client.get_block(page_url)

        prev_list = {}
        for child in page.children:
            norm = child.title.lower().strip()
            if norm not in prev_list:
                prev_list[norm] = child
                continue

            prev_child = prev_list[norm]

            if not child.checked and prev_child.checked:
                prev_child.checked = False

            child.remove(permanently=True)



