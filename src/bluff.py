import uuid
import random
import itertools
from typing import Dict, List, NoReturn

from cards import Deck
from player import Player
from game import Game


class Gamerunner:
    def __init__(self):
        pass
        

def main():
    d = Deck()
    p = [Player('asdfs', 'sachin'), Player('sss', 'ticks'), Player('ddd', 'sachsain'), Player('r', 'ss')]
    g = Game(p)



if __name__=="__main__":
    main()