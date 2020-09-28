import os

from handlers.shop_list_handler.handler import handler

os.environ['page_url'] = 'https://www.notion.so/762a5a2cb95b48848af8752ca7336898'
os.environ[
    'token_v2'] = '098a4f3ea3d86283e123f3dd41ec2d0d0bab865032aee44dfe3a85454eb2faeb8389446453727a338cf606d9e307a2fcf91ad53c810510415703156619a193df728ed9d2580f836dd3c3b6d5a950'


handler({
    "meta": {
        "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
        "interfaces": {
            "account_linking": {},
            "payments": {},
            "screen": {}
        },
        "locale": "ru-RU",
        "timezone": "UTC"
    },
    "request": {
        "original_utterance": "Кофе",
        "command": "",
        "nlu": {
            "entities": [],
            "tokens": []
        },
        "type": "SimpleUtterance"
    },
    "session": {
        "message_id": 0,
        "new": 'true',
        "session_id": "1c6c406c-c777-4b7f-8269-6ec4369319ad",
        "skill_id": "4f093d27-be1c-4324-998b-683f68700a66",
        "user_id": "45eb09c1-c32c-4405-bad7-7b716a9dc7d7"
    },
    "version": "1.0"
}, {})