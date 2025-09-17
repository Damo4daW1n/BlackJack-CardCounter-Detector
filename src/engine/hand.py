from .card import Card, Rank

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def value(self):
        total = sum(c.value for c in self.cards)
        # Handle aces as 1 or 11
        aces = sum(1 for c in self.cards if c.rank == Rank.ACE)
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def is_blackjack(self):
        return len(self.cards) == 2 and self.value() == 21

    def is_bust(self):
        return self.value() > 21

    def __repr__(self):
        return f"{' '.join(str(c) for c in self.cards)} ({self.value()})"
