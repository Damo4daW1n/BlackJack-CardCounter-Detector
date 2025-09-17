import enum

class Suit(enum.Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"

class Rank(enum.Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    @property
    def value(self) -> int:
        if self.rank in {Rank.JACK, Rank.QUEEN, Rank.KING, Rank.TEN}:
            return 10
        if self.rank == Rank.ACE:
            return 11
        return int(self.rank.value)

    def __repr__(self) -> str:
        return f"{self.rank.value}{self.suit.value}"
