from .deck import Shoe
from .hand import Hand

class BlackjackGame:
    def __init__(self, num_decks=6, starting_chips=1000):
        self.shoe = Shoe(num_decks)
        self.chips = starting_chips
        self.bet = 1

    def play_round(self, player_strategy):
        # Deal initial hands
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(self.shoe.deal())
        dealer_hand.add_card(self.shoe.deal())
        player_hand.add_card(self.shoe.deal())
        dealer_hand.add_card(self.shoe.deal())

        print(f"\n--- New Round ---")
        print(f"Chips: {self.chips}")
        print(f"Dealer upcard: {dealer_hand.cards[0]}")

        # Player loop
        while not player_hand.is_bust():
            action = player_strategy.decide(player_hand, dealer_hand.cards[0])

            if action == "stand":
                break
            elif action == "hit":
                player_hand.add_card(self.shoe.deal())
                print(f"You drew: {player_hand.cards[-1]} (Now: {player_hand})")
            elif action == "double":
                if self.chips >= self.bet:
                    self.bet *= 2
                    player_hand.add_card(self.shoe.deal())
                    print(f"You doubled! Drew {player_hand.cards[-1]}")
                break
            elif action == "split":
                print("Splits not implemented yet — treating as stand.")
                break
            elif action == "insurance":
                print("Insurance not implemented yet — treating as stand.")
                break

        # Dealer plays
        while dealer_hand.value() < 17:
            dealer_hand.add_card(self.shoe.deal())

        outcome = self._determine_winner(player_hand, dealer_hand)
        self._settle_bet(outcome)

        print(f"\nDealer hand: {dealer_hand}")
        print(f"Your hand:   {player_hand}")
        print(f"Outcome: {outcome}")
        print(f"Chips left: {self.chips}")

        return outcome

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

    def _settle_bet(self, outcome):
        if outcome == "win":
            self.chips += self.bet
        elif outcome == "lose":
            self.chips -= self.bet
        # push = no change
        self.bet = 1  # reset bet
