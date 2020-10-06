from Constants import constants
from Services.notion.UnofficialNotionAPI import NotionAPI

NotionAPI().sort_todos(constants.ShoppingListURL)

