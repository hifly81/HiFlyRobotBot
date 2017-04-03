import requests
from config import BotConfig


class BotOperation:

    def __init__(self):
        token = BotConfig.get_property('SECURITY', 'bot_token')
        self.api_url = BotConfig.get_property('API', 'telegram_url') + "{}/".format(token)

    def send_unrecognized_message(self, chat_id):
        """Send a text message to telegram.
        Need the chat_id
        """
        params = {'chat_id': chat_id, 'text': "Sorry but I can't recognize your question! Try with another one..."}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_message(self, chat_id, text):
        """Send a text message to telegram.
        Need the chat_id
        """
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_photo(self, chat_id, files, caption):
        """Send a photo message to telegram with its caption
        Need the chat_id
        """
        params = {'chat_id': chat_id, 'caption': caption}
        method = 'sendPhoto'
        resp = requests.post(self.api_url + method, data=params, files=files)
        return resp
