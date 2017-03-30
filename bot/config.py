import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('bot.properties')


class BotConfig(object):
    @staticmethod
    def get_property(section, prop):
        return config.get(section, prop)
