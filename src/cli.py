from engine.game import BlackjackGame
from players.human_player import HumanPlayer

def main():
    game = BlackjackGame()
    player = HumanPlayer()

    while game.chips > 0:
        outcome = game.play_round(player)
        cont = input("\nPlay another round? (y/n): ").strip().lower()
        if cont != "y":
            break

    print("\nGame over. Thanks for playing!")

if __name__ == "__main__":
    main()
