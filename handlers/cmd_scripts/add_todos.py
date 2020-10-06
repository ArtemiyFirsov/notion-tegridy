import sys

from Constants import constants
from Services.notion.UnofficialNotionAPI import NotionAPI

NotionAPI().add_todos(constants.ShoppingListURL, sys.argv[1].split(" и "))