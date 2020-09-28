import notion.client as client
import sys

token_v2 = sys.argv[1]
page_url = sys.argv[2]
todos = sys.argv[3:]

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = client.NotionClient(token_v2=token_v2)

# Replace this URL with the URL of the page you want to edit
page = client.get_block(page_url)

for arg in todos:
	previous = [i for i in page.children if i.title.lower().strip() == arg.lower().strip()]
	if len(previous) > 0:
		child = previous[0]
		child.checked = False
	else:
		child = page.children.add_new(block.basic.ToDoBlock, title=arg)
	if len(page.children) > 0 and child.url != page.children[0].url:
		child.move_to(page.children[0], "before")