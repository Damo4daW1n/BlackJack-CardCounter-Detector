class BasePlayer:
    def decide(self, hand, dealer_upcard):
        raise NotImplementedError("Players must implement decide()")
