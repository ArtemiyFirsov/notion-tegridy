import notion.block as block
import notion.client as clientModule
from typing import List

from Constants import constants
from Services.BaseNotionWrapper import BaseNotionAPI


class NotionAPI(BaseNotionAPI):
    def add_todos(self, todos: List[str]):
        token_v2 = constants.NotionTokenV2
        page_url = constants.ShoppingListURL

        client = clientModule.NotionClient(token_v2=token_v2)
        page = client.get_block(page_url)

        for arg in todos:
            previous = [i for i in page.children if i.title.lower().strip() == arg.lower().strip()]
            if len(previous) > 0:
                child = previous[0]
                child.checked = False
            else:
                child = page.children.add_new(block.TodoBlock, title=arg)
            if len(page.children) > 0 and child.id != page.children[0].id:
                child.move_to(page.children[0], "before")
