import os
import sys
import notion.block as block

from Constants import constants
from notion.client import NotionClient

from Services.UnofficialNotionAPI import NotionAPI

os.environ["NOTION_DATA_DIR"] = constants.NotionCachePath

NotionAPI().sort_todos(constants.ShoppingListURL)

