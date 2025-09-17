import pytest
from src.engine.deck import Shoe

def test_shoe_deals_cards():
    shoe = Shoe(1)
    card = shoe.deal()
    assert card is not None
    assert shoe.remaining() == 51
