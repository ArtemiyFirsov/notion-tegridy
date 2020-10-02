import os
import sys
import notion.block as block

from Constants import constants
from notion.client import NotionClient

os.environ["NOTION_DATA_DIR"] = constants.NotionCachePath

token_v2 = constants.NotionTokenV2
page_url = constants.ShoppingListURL

client = NotionClient(token_v2=token_v2)
page = client.get_block(page_url)

children_filtered = [i for i in page.children if type(i) == block.TodoBlock and i.title]
unchecked_count = len([i for i in page.children if not i.checked])
curr_unchecked_count = 0
for i, child in enumerate(children_filtered):
    if curr_unchecked_count == unchecked_count:
        break
    if not child.checked and i > 0:
        child.move_to(page.children[0], "before")
        curr_unchecked_count += 1
