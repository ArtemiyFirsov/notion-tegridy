import logging

from Constants import constants
from Helpers.Thread import RunInThread
from Services.notion.UnofficialNotionAPI import NotionAPI


# todo: it is now broken
def handler(event, context):
    is_final_message = False
    logging.info(event)

    if 'session' in event and 'new' in event['session'] and event['session']['new']:
        text = "скажите, что вы собираетесь купить"
    elif 'request' in event and \
            'original_utterance' in event['request'] \
            and len(event['request']['original_utterance']) > 0:
        text = 'отправила на добавление'
        request = event['request']['original_utterance']
        is_final_message = True
        RunInThread(NotionAPI(TOKEN_V2).add_todos, SHOPPING_LIST_URL, request.split(" и "))l
    else:
        text = "что-то пошло не так"
        is_final_message = True

    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': text,
            'end_session': is_final_message
        }
    }
