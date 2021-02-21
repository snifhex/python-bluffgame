import random
import itertools
from typing import List, NoReturn


class Card:
    """
    A class For single card which has rank, suit and its color
    """
    colors = ('black', 'red')
    suits = ('spades', 'clubs', 'hearts', 'diamonds')
    ranks = ('narf', 'ace','2','3','4','5','6','7','8','9','10', 'jack', 'queen', 'king')
    
    def __init__(self, rank, suit, color=None, **kwargs) -> NoReturn:
        index = kwargs.get('index', False)

        if index:
            self.rank = self.ranks[rank]
            self.suit = self.suits[suit]
            self.color = self.colors[color]
        else:
            self.rank = rank
            self.suit = suit
            self.color = color

    def __str__(self) -> str:
        return f"Card of rank {self.rank} in {self.suit} suit of {self.color}"

class Deck:
    """
    A class for creating a single deck or a deck with multiple decks.
    """

    special_ranks = ['joker']
    colors =  ['red', 'black']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    ranks = ['2','3','4','5','6','7','8','9','10', 'ace', 'queen', 'king', 'jack']


    def __init__(self) -> NoReturn:
        self.deck = self.create_deck()
        self.deck_size = len(self.deck)

    def create_deck(self, no_of_deck: int=None) -> List[Card]:
        """
        Creating a deck takes one integer input as positional argument, 
        if none given it will create a deck of cards with 54 cards.
        """
        self.bare_deck = list(itertools.product(self.ranks, self.suits)) + [(self.special_ranks, self.special_ranks, 'black'), (self.special_ranks, self.special_ranks, 'red')]
        deck = [Card(d[0], d[1]) for d in self.bare_deck]
        # deck = self.ranks*4 + self.special_ranks
        if no_of_deck:
            deck = deck*no_of_deck
        return deck

    def add_new_deck(self) -> List[Card]:
        """
        """
        deck = self.deck*self.bare_deck()
        return deck

    def shuffle(self) -> List[Card]:
        """
        Shuffles the deck
        """
        return random.shuffle(self.deck)
    
    def draw(self) -> List[Card]:
        self.deck
    
    def pop(self):
        return self.deck.pop()

    def __str__(self):
        return f"BareDeck: {self.bare_deck}"

class Hand:
    def __init__(self):
        pass