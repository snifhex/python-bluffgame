import math
import random
from typing import List
from cards import Card,Deck
from player import Player

class Game:
    MIN_PLAYER_LIMIT = 2
    MAX_PLAYER_LIMIT = 12

    def __init__(self, players: List[Player]=[]):
        self.players = players
        self.no_of_players = len(players)
        
    def _draw_cards(self, deck, total_cards: int=1):
        hand = []
        for _ in range(total_cards):
            hand.append(deck.pop())
        return hand

    def _allocate_cards(self):

        if self.no_of_players < self.MIN_PLAYER_LIMIT:
            raise Exception("MIN PLAYER LIMIT")
        if self.no_of_players > self.MAX_PLAYER_LIMIT:
            raise Exception('MAX PLAYER LIMIT')

        distribution = []
        deck = Deck()
        cards_per_player = math.floor(deck.deck_size/self.no_of_players)

        for _ in range(self.no_of_players):
            distribution.append(self._draw_cards(deck.deck,cards_per_player))
            for player, cards in zip(self.players, distribution):
                player.cards = cards
                
        if len(deck.deck):
            for _ in range(len(deck.deck)):
                random.choice(distribution).append(deck.deck.pop())
        

if __name__=="__main__":
    pass
