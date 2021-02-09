import sys
from Constants import constants
from Services.notion.UnofficialNotionAPI import NotionAPI

notion_token_v2 = sys.argv[1]
shopping_list_URL = sys.argv[2]

NotionAPI(notion_token_v2).sort_todos(shopping_list_URL)

