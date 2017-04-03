import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('bot.properties')


class BotConfig(object):
    @staticmethod
    def get_property(section, prop):
        return config.get(section, prop)

    @staticmethod
    def get_greetings():
        greetings_dict = {}
        greetings_list = config.get('MESSAGES', 'greetings').split(',')
        for greet in greetings_list:
            terms = greet.split('-')
            greetings_dict[terms[0]] = terms[1]
        return greetings_dict

