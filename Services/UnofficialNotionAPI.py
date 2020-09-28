from typing import List
import notion.client as clientModule
import notion.block as block
import os

from Services.BaseNotionWrapper import BaseNotionAPI


class NotionAPI(BaseNotionAPI):
    def add_todos(self, todos: List[str]):
        token_v2 = os.environ["token_v2"]
        page_url = os.environ["page_url"]

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
