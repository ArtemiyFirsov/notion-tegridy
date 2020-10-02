import notion.client as client
import sys

from Constants import constants
from Services.UnofficialNotionAPI import NotionAPI

NotionAPI().add_todos(constants.ShoppingListURL, sys.argv[1].split(" и "))