from engine.game import BlackjackGame
from players.basic_strategy import BasicStrategyPlayer

def main():
    game = BlackjackGame()
    player = BasicStrategyPlayer()

    for i in range(5):
        p_hand, d_hand, outcome = game.play_round(player)
        print(f"Round {i+1}:")
        print(f"  Player: {p_hand}")
        print(f"  Dealer: {d_hand}")
        print(f"  Outcome: {outcome}\n")

if __name__ == "__main__":
    main()
