import random
from .card import Card, Suit, Rank

class Shoe:
    def __init__(self, num_decks: int = 6):
        self.num_decks = num_decks
        self.cards = self._generate_shoe()
        random.shuffle(self.cards)

    def _generate_shoe(self):
        return [
            Card(rank, suit)
            for _ in range(self.num_decks)
            for suit in Suit
            for rank in Rank
        ]

    def deal(self):
        if not self.cards:
            raise ValueError("Shoe is empty, reshuffle required.")
        return self.cards.pop()

    def remaining(self):
        return len(self.cards)
