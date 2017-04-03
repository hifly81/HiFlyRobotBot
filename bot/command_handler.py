import os.path

from parsers import wikipedia, youtube, words
from config import BotConfig
from bot.operation import BotOperation


class BotCommandHandler:
    wiki = wikipedia.WikipediaParser()
    youtube = youtube.YoutubeParser()
    words = words.WordsMatcher()
    bot_operation = BotOperation()

    def __init__(self):
        token = BotConfig.get_property('SECURITY', 'bot_token')
        self.api_url = BotConfig.get_property('API', 'telegram_url') + "{}/".format(token)

    def dispatch(self, last_chat_text, last_chat_id, last_chat_username):
        """Parse the incoming command from client
        and dispatch to the right handler
        """

        if self.start(last_chat_text, last_chat_id) is None:
            if self.greet(last_chat_text, last_chat_id, last_chat_username) is None:
                if self.country(last_chat_text, last_chat_id) is None:
                    if self.jazz(last_chat_text, last_chat_id) is None:
                        self.bot_operation.send_unrecognized_message(last_chat_id)

    def start(self, message, chat_id):
        """The bot sends a startup message
        """

        if message == '/start':
            return self.bot_operation(chat_id, 'Welcome to HiflyRobotBot! I\'m happy to help you!')
        else:
            return None

    def greet(self, message, chat_id, username):
        """The bot greets you
        """
        message = message.lower()
        greets = BotConfig.get_greetings()
        message_key = self.words.find_greeting(message, greets)
        if message_key is not None:
            return self.bot_operation.send_message(chat_id, 'Hey, welcome {}'.format(username) + '. Maybe you are ' + greets[message_key])
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
                return self.bot_operation.send_photo(chat_id, files, self.wiki.get_country_page(country_code))
            else:
                return None
        else:
            return None

    def jazz(self, message, chat_id):
        """The bot reacts to a /jazz command
        """

        if message == '/jazz':
            result = self.youtube.get_random_playlist_result(message)
            if result is not None:
                return self.bot_operation.send_message(chat_id, result)
            else:
                return None
        else:
            return None
