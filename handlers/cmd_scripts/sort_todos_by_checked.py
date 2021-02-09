import sys
from Constants import constants
from Services.notion.UnofficialNotionAPI import NotionAPI

#notion_token_v2 = sys.argv[1]
#shopping_list_URL = sys.argv[2]

notion_token_v2 = "9f176e58d5cd88e1a2245f3a88cc9e7d89d1a3a9a77a4d95f038add06068c9563c4ff5e1566c3dccb5005ad3f49b44a96f95df3d86aaf80761c2a059a4d7ff48950e0ff758494adabff297a7f5a2"
shopping_list_URL = "https://www.notion.so/762a5a2cb95b48848af8752ca7336898"

NotionAPI(notion_token_v2).sort_todos(shopping_list_URL)

