from .base_player import BasePlayer

class BasicStrategyPlayer(BasePlayer):
    def decide(self, hand, dealer_upcard):
        # Placeholder: always hit below 17, else stand
        return "hit" if hand.value() < 17 else "stand"
