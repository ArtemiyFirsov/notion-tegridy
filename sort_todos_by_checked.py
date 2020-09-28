from notion.client import NotionClient
import notion.block as block


token_v2 = sys.argv[1]
page_url = sys.argv[2]
todos = sys.argv[3:]

client = NotionClient(token_v2=token_v2)
page = client.get_block(page_url)

first_unchecked = None

for child in page.children:
	if type(child) != block.basic.ToDoBlock or \
		not child.title:
		continue
	if not child.checked:
		if not first_unchecked:
			first_unchecked = child
		else:
			child.move_to(first_unchecked, "after")
	else:
		child.move_to(page.children[-1], "after")