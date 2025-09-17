from src.engine.hand import Hand
from src.engine.card import Card, Rank, Suit

def test_hand_value_with_aces():
    hand = Hand()
    hand.add_card(Card(Rank.ACE, Suit.HEARTS))
    hand.add_card(Card(Rank.SIX, Suit.SPADES))
    assert hand.value() == 17

    hand.add_card(Card(Rank.NINE, Suit.CLUBS))
    assert hand.value() == 16
