import sys
from Constants import constants
from Services.notion.UnofficialNotionAPI import NotionAPI

notion_token_v2 = sys.argv[1]
shopping_list_URL = sys.argv[2]
items = sys.argv[3].split(" и ")

NotionAPI(notion_token_v2).add_todos(shopping_list_URL, sys.argv[3].split(" и "))