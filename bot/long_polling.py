import requests
from config import BotConfig


class BotLongPolling:

    def __init__(self):
        token = BotConfig.get_property('SECURITY', 'bot_token')
        self.api_url = BotConfig.get_property('API', 'telegram_url') + "{}/".format(token)

    def last_message(self, offset=None, timeout=10):
        """Get the last message from telegram.
        It reproduces a long polling with a timeout of 10 seconds
        """

        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']

        if len(result_json) > 0:
            last_message = result_json[-1]
        else:
            last_message = None

        return last_message
