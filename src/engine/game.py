from .deck import Shoe
from .hand import Hand

class BlackjackGame:
    def __init__(self, num_decks=6, starting_chips=1000):
        self.shoe = Shoe(num_decks)
        self.starting_chips = starting_chips
        self.chips = starting_chips

    def play_round(self, player_strategy):
        # Deal initial hands
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(self.shoe.deal())
        dealer_hand.add_card(self.shoe.deal())
        player_hand.add_card(self.shoe.deal())
        dealer_hand.add_card(self.shoe.deal())

        # Player decision loop
        while not player_hand.is_bust():
            action = player_strategy.decide(player_hand, dealer_hand.cards[0])
            if action == "stand":
                break
            elif action == "hit":
                player_hand.add_card(self.shoe.deal())
            else:
                # doubles, splits, insurance -> placeholders
                break

        # Dealer logic: hits until 17+
        while dealer_hand.value() < 17:
            dealer_hand.add_card(self.shoe.deal())

        # Determine outcome
        outcome = self._determine_winner(player_hand, dealer_hand)
        return player_hand, dealer_hand, outcome

    def _determine_winner(self, player, dealer):
        if player.is_bust():
            return "lose"
        if dealer.is_bust():
            return "win"
        if player.value() > dealer.value():
            return "win"
        if player.value() < dealer.value():
            return "lose"
        return "push"
