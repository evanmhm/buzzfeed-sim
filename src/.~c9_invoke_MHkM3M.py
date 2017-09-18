import requests
import json
from markov import MarkovChain

class BuzzfeedManager:
    def __init__(self):
        self.titles = []
        
    def get(self, query, page):
        r = requests.get('http://www.buzzfeed.com/api/v2/feeds/'+query'?p='+page)
        self.buzzfeed_json = r.json()
        
        
        for page in range(pages):
        for page in range(pages):
            for buzz in self.buzzfeed_json['buzzes']:
                print buzz['title'].replace('&quot;', '\'')


if __name__ == '__main__':
    buzzfeed = BuzzfeedManager()
    buzzfeed.get('lol')
    buzzfeed.train()
    # print buzzfeed.buzzfeed_json['buzzes'][7]['title']