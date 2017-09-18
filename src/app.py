#!/usr/bin/env python

import src.markov as markov
from markov import MarkovChain
from buzzfeedmanager import BuzzfeedManager

from . import args

class MarkovMusic:

    def __init__(self):
        self.args = args

    def run(self):
        mc = MarkovChain(1)
        manager = BuzzfeedManager('lol')
        training_data = manager.read_titles()
        
        for title in training_data:
            mc.add_string(title)
        
        markovOut = ' '.join(mc.generate_text(22))
        print markovOut