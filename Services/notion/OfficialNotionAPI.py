from typing import List
import httpx
from Services.notion.BaseNotionWrapper import BaseNotionAPI


class NotionAPI(BaseNotionAPI):
    def __init__(self, notion_token: str):
        self._token = notion_token

    def add_todos(self, page_url: str, todos: List[str]):
        with httpx.Client() as client:
            headers = {
                'Authorization': f'Bearer {self._token}',
                'Notion-Version': '2021-05-13'
            }
            r = client.get(page_url, headers=headers)
        jsn = r.json()

        print(r)
        #for arg in todos:
        #    previous = [i for i in page.children if i.title.lower().strip() == arg.lower().strip()]
        #    if len(previous) > 0:
        #        child = previous[0]
        #        child.checked = False
        #    else:
        #        child = page.children.add_new(block.TodoBlock, title=arg)
        #    if len(page.children) > 0 and child.id != page.children[0].id:
        #        child.move_to(page.children[0], "before")

    def sort_todos(self, page_url: str):
        page = self._client.get_block(page_url)

        children_filtered = {i: v for i, v in enumerate(page.children) if
                             type(v) == block.TodoBlock and v.title and not v.checked}

        for ind, child in children_filtered.items():
            if child.id == page.children[0].id:
                continue

            if not page.children[ind - 1].checked:
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

NotionAPI('secret_qrWMROFomPvS8hNGmPz65PQJ7y0nzoJdRIateQFNdZ1').add_todos('https://api.notion.com/v1/blocks/762a5a2c-b95b-4884-8af8-752ca7336898/children', todos=["test"])