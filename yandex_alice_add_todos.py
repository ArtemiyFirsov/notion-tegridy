import logging
import os

os.environ["NOTION_DATA_DIR"] = os.path.join("/tmp", ".notion-py")

def handler(event, context):
    text = 'добавила'
    if 'request' in event and \
            'original_utterance' in event['request'] \
            and len(event['request']['original_utterance']) > 0:
        text = event['request']['original_utterance']
        try:
            addtodos(text.split(","))
        except Exception as e:
            text = "не получилось"
            logging.exception(e)
            pass
            
    else:
        text = "нечего добавить"
        
    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': text,
            'end_session': 'true'
        },
    }
    
def addtodos(todos):
    import notion.client as client
    import notion.block as block
    import sys
    import os
    
    token_v2 = os.environ["token_v2"]
    page_url = os.environ["page_url"]
    
    client = client.NotionClient(token_v2=token_v2)
    page = client.get_block(page_url)
    
    for arg in todos:
    	previous = [i for i in page.children if i.title.lower().strip() == arg.lower().strip()]
    	if len(previous) > 0:
    		child = previous[0]
    		child.checked = False
    	else:
    		child = page.children.add_new(block.TodoBlock, title=arg)
    	if len(page.children) > 0 and child.url != page.children[0].url:
    		child.move_to(page.children[0], "before")