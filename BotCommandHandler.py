import requests
import os.path
from BotConfig import BotConfig
from WikipediaParser import WikipediaParser


class BotCommandHandler:
    greetings = ('ciao', 'salve', 'hello', 'hi', 'priviet')
    wiki = WikipediaParser()

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

    def dispatch(self, last_chat_text, last_chat_id, last_chat_username):
        """Parse the incoming command from client
        and dispatch to the right handler
        """

        if self.start(last_chat_text, last_chat_id) is None:
            if self.greet(last_chat_text, last_chat_id, last_chat_username) is None:
                if self.country(last_chat_text, last_chat_id) is None:
                    self.send_unrecognized_message(last_chat_id)

    def start(self, message, chat_id):
        """The bot sends a startup message
        """

        if message == '/start':
            return self.send_message(chat_id, 'Welcome to HiflyRobotBot! I\'m happy to help you!')
        else:
            return None

    def greet(self, message, chat_id, username):
        """The bot greets you
        """

        message = message.lower()

        if message in self.greetings:
            return self.send_message(chat_id, 'Hey, welcome {}'.format(username))
        else:
            return None

    def country(self, message, chat_id):
        """The bot reacts to a /<country_code> command
        """

        country_code_len = len(message)
        country_code = message[1:3].lower()
        image_path = 'countries/' + country_code.lower() + '.png'

        if os.path.exists(image_path) and country_code_len <= 4:
            files = {'photo': (image_path, open(image_path))}
            country_wiki_page = self.wiki.get_country_page(country_code)
            if country_wiki_page is not None:
                return self.send_photo(chat_id, files, self.wiki.get_country_page(country_code))
            else:
                return None
        else:
            return None
