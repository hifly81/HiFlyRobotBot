import urllib2

from lxml import etree

from bot.config import BotConfig


class WikipediaParser:

    def __init__(self):
        pass

    def get_country_page(self, country_code):
        """Get ENG wikipedia page for country;
        it is based on scraping of wikipedia page https://en.wikipedia.org/wiki/ISO_3166-1
        """

        wikipedia_country_url = BotConfig.get_property('WIKIPEDIA', 'country_url')
        country_code = country_code.upper()
        data = urllib2.urlopen(wikipedia_country_url).read()
        # return the root node of html document
        doc = etree.HTML(data)

        for span in doc.iter('span'):
            # found country code
            if span.text == country_code:
                try:
                    country_wiki_page = span.getparent().getparent().getparent().getchildren()[0].getchildren()[0].get(
                        'href')
                    return BotConfig.get_property('WIKIPEDIA', 'wikipedia_base_url') + country_wiki_page
                except:
                    return None
