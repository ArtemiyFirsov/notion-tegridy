from Constants import constants
from Services.notion.UnofficialNotionAPI import NotionAPI

NotionAPI().delete_todos_duplicates(constants.ShoppingListURL)

