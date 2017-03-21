#!/usr/bin/env python

"""
Usage:
python hifly_robot_bot.sh
Ctrl-C or kill the process to stop the bot.
"""

from BotLongPolling import BotLongPolling
from BotCommandHandler import BotCommandHandler


bot = BotLongPolling()
bot_command_handler = BotCommandHandler()


def main():
    """Listen for telegram incoming messages
    """

    message_index = None

    while True:

        last_message = bot.last_message(message_index)

        if last_message is not None:
            last_message_id = last_message['update_id']
            last_chat_text = last_message['message']['text']
            last_chat_id = last_message['message']['chat']['id']
            last_chat_username = last_message['message']['chat']['first_name']

            bot_command_handler.dispatch(last_chat_text, last_chat_id, last_chat_username)

            message_index = last_message_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()