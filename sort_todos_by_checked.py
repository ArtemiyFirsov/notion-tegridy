import os
import sys

os.environ["NOTION_DATA_DIR"] = "/private/var/mobile/Containers/Shared/AppGroup/0E89090C-35CC-4B33-A31D-9A297BB590C1/File Provider Storage/Repositories/notion-tegridy/.notion-py"

from notion.client import NotionClient
import notion.block as block


token_v2 = sys.argv[1]
page_url = sys.argv[2]

client = NotionClient(token_v2=token_v2)
page = client.get_block(page_url)

print(token_v2, page_url)


children_filtered = [i for i in page.children if type(i) == block.basic.ToDoBlock and i.title]
unchecked_count = len([i for i in page.children if not i.checked])
curr_unchecked_count = 0
for i, child in enumerate(children_filtered):
    if curr_unchecked_count == unchecked_count:
        break
    if not child.checked and i > 0:
        child.move_to(page.children[0], "before")
        curr_unchecked_count += 1