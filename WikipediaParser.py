from BotConfig import BotConfig
from lxml import etree
import urllib2


class WikipediaParser:
    def __init__(self):
        self.wikipedia_country_url = BotConfig.get_property('WIKIPEDIA', 'country_url')

    def get_country_page(self, country_code):
        """Get ENG wikipedia page for country;
        it is based on scraping of wikipedia page https://en.wikipedia.org/wiki/ISO_3166-1
        """

        country_code = country_code.upper()
        data = urllib2.urlopen(self.wikipedia_country_url).read()
        # return the root node of html document
        doc = etree.HTML(data)

        for span in doc.iter('span'):
            # found country code
            if span.text == country_code:
                country_wiki_page = span.getparent().getparent().getparent().getchildren()[0].getchildren()[0].get('href')
                return BotConfig.get_property('WIKIPEDIA', 'wikipedia_base_url') + country_wiki_page
