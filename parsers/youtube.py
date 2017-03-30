import random
import urllib2

from bs4 import BeautifulSoup
from bot.config import BotConfig


class YoutubeParser:

    def __init__(self):
        pass

    def get_random_playlist_result(self, text_to_search):
        """Get Search Result from Youtube
        """

        youtube_search_url = BotConfig.get_property('YOUTUBE', 'search_url')
        query = urllib2.quote(text_to_search)
        #find only_playlist
        url = youtube_search_url + query + ',playlist'
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        for link in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            links.append(BotConfig.get_property('YOUTUBE', 'base_url') + link['href'])
        if len(links) > 0:
            return random.choice(links)
        else:
            return None
