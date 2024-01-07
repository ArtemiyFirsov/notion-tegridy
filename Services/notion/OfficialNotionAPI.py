from typing import List
import httpx
from notion_client import Client

from BaseNotionWrapper import BaseNotionAPI



class NotionAPI(BaseNotionAPI):
    def __init__(self, notion_token: str):
        self._token = notion_token
        self._notion = Client(auth=self._token)

    def _list_page_blocks(self, page_id: str):
        page_blocks = []
        
        next_cursor = None
        page_size=100
        while True:
            page_chunk = self._notion.blocks.children.list(page_id, page_size=page_size, start_cursor=next_cursor)
            page_blocks += page_chunk["results"]

            if not page_chunk["has_more"]:
                break

            next_cursor = page_chunk["next_cursor"]
        
        return page_blocks
    
    def _update_todo_counter(self, page_url: str):
        page_id = [i for i in page_url.split("/") if len(i) > 0][-1]
        page_blocks = self._list_page_blocks(page_id)

        todo_len = len([i for i in page_blocks if i['type'] == "to_do"])

        self._notion.blocks.update(block_id=page_blocks[0]["id"], paragraph={"rich_text": [{"text": { "content": f"Список покупок ({todo_len})" } }]})


    def add_todos(self, page_url: str, todos: List[str]):
        page_id = [i for i in page_url.split("/") if len(i) > 0][-1]
        page_blocks = self._list_page_blocks(page_id)

        old_todos = [
            {
                "id": to_do['id'],
                "text": to_do['to_do']['rich_text'][0]['plain_text']
            } for to_do in page_blocks if to_do['type'] == "to_do" and len(to_do['to_do']['rich_text']) > 0]

        append_after = page_blocks[0]["id"]

        for new_todo in todos:
            self._notion.blocks.children.append(page_id, children=[{
                                                            "type": "to_do",
                                                            "to_do": {
                                                                "rich_text": [{
                                                                "type": "text",
                                                                "text": {
                                                                    "content": new_todo
                                                                }
                                                            }],
                                                            "checked": False,
                                                            "color": "default",
                                                            }}], 
                                                after=append_after)
            
            previous = [i for i in old_todos if i["text"].lower().strip() == new_todo.lower().strip()]
            for prev in previous:
                self._notion.blocks.delete(prev["id"])

        self._update_todo_counter(page_url)
            

    def sort_todos(self, page_url: str):
        page_id = [i for i in page_url.split("/") if len(i) > 0][-1]
        page_blocks = self._list_page_blocks(page_id)

        not_resolved_todos = [
            {
                "id": to_do['id'],
                "text": to_do['to_do']['rich_text'][0]['plain_text']
            } for to_do in page_blocks if to_do['type'] == "to_do" and len(to_do['to_do']['rich_text']) > 0 and not to_do['to_do']['checked']]

        append_after = page_blocks[0]["id"]

        for todo in not_resolved_todos:
            self._notion.blocks.children.append(page_id, children=[{
                                                            "type": "to_do",
                                                            "to_do": {
                                                                "rich_text": [{
                                                                "type": "text",
                                                                "text": {
                                                                    "content": todo["text"]
                                                                }
                                                            }],
                                                            "checked": False,
                                                            "color": "default",
                                                            }}], 
                                                after=append_after)

            self._notion.blocks.delete(todo["id"])

    def delete_todos_duplicates(self, page_url: str):
        page_id = [i for i in page_url.split("/") if len(i) > 0][-1]
        page_blocks = self._list_page_blocks(page_id)

        old_todos = [
            {
                "id": to_do['id'],
                "text": to_do['to_do']['rich_text'][0]['plain_text'],
                "checked": to_do['to_do']['checked']
            } for to_do in page_blocks if to_do['type'] == "to_do" and len(to_do['to_do']['rich_text']) > 0]
        
        prev_list = {}
        for child in old_todos:
            norm = child["text"].lower().strip()
            if norm not in prev_list:
                prev_list[norm] = child
                continue

            prev_child = prev_list[norm]

            if not child["checked"] and prev_child["checked"]:
                self._notion.blocks.update(block_id=prev_child["id"], to_do={"checked": False})

            self._notion.blocks.delete(block_id=child["id"])
        
        self._update_todo_counter(page_url)