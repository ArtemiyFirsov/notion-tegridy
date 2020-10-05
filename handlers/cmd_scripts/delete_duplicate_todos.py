from Constants import constants
from Services.UnofficialNotionAPI import NotionAPI

NotionAPI().delete_todos_duplicates(constants.ShoppingListURL)

