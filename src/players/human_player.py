from .base_player import BasePlayer

class HumanPlayer(BasePlayer):
    def decide(self, hand, dealer_upcard):
        print(f"\nYour hand: {hand}")
        print(f"Dealer shows: {dealer_upcard}")

        valid_actions = ["hit", "stand", "double", "split", "insurance"]
        while True:
            action = input(f"Choose action ({'/'.join(valid_actions)}): ").strip().lower()
            if action in valid_actions:
                return action
            print("Invalid action. Try again.")
