import os
from Constants import constants
from Services.UnofficialNotionAPI import NotionAPI

os.environ["NOTION_DATA_DIR"] = constants.NotionCachePath

NotionAPI().sort_todos(constants.ShoppingListURL)

