import os

import sys

from Constants import constants
from Services.UnofficialNotionAPI import NotionAPI

os.environ["NOTION_DATA_DIR"] = constants.NotionCachePath

NotionAPI().add_todos(constants.ShoppingListURL, sys.argv[1].split(" и "))