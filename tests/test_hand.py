from src.main import Card, Hand, Colour, Value, HandStrength


def test_is_hand_strength_flush():
    assert Hand(
        [
            Card(Colour.CLUBS, Value.TWO),
            Card(Colour.CLUBS, Value.FOUR),
            Card(Colour.CLUBS, Value.SIX),
            Card(Colour.CLUBS, Value.EIGHT),
            Card(Colour.CLUBS, Value.TEN),
            Card(Colour.DIAMONDS, Value.QUEEN),
            Card(Colour.HEARTS, Value.ACE)
        ]
    ).get_hand_strength() == HandStrength.FLUSH


def test_is_not_hand_strength_flush():
    assert Hand(
        [
            Card(Colour.SPADES, Value.TWO),
            Card(Colour.DIAMONDS, Value.FOUR),
            Card(Colour.HEARTS, Value.SIX),
            Card(Colour.CLUBS, Value.EIGHT),
            Card(Colour.SPADES, Value.TEN),
            Card(Colour.DIAMONDS, Value.QUEEN),
            Card(Colour.HEARTS, Value.ACE)
        ]
    ).get_hand_strength() != HandStrength.FLUSH


def test_is_hand_strength_two_pair():
    assert Hand(
        [
            Card(Colour.CLUBS, Value.TWO),
            Card(Colour.HEARTS, Value.TWO),
            Card(Colour.DIAMONDS, Value.SIX),
            Card(Colour.SPADES, Value.SIX),
            Card(Colour.CLUBS, Value.TEN),
            Card(Colour.HEARTS, Value.QUEEN),
            Card(Colour.DIAMONDS, Value.ACE)
        ]
    ).get_hand_strength() == HandStrength.TWO_PAIR


def test_is_not_hand_strength_two_pair():
    assert Hand(
        [
            Card(Colour.CLUBS, Value.TWO),
            Card(Colour.HEARTS, Value.THREE),
            Card(Colour.DIAMONDS, Value.SIX),
            Card(Colour.SPADES, Value.SIX),
            Card(Colour.CLUBS, Value.TEN),
            Card(Colour.HEARTS, Value.QUEEN),
            Card(Colour.DIAMONDS, Value.ACE)
        ]
    ).get_hand_strength() != HandStrength.TWO_PAIR


def test_is_hand_strength_three_of_a_kind():
    assert Hand(
        [
            Card(Colour.CLUBS, Value.TWO),
            Card(Colour.HEARTS, Value.TWO),
            Card(Colour.DIAMONDS, Value.TWO),
            Card(Colour.SPADES, Value.SIX),
            Card(Colour.CLUBS, Value.TEN),
            Card(Colour.HEARTS, Value.QUEEN),
            Card(Colour.DIAMONDS, Value.ACE)
        ]
    ).get_hand_strength() == HandStrength.THREE_OF_A_KIND


def test_is_not_hand_strength_three_of_a_kind():
    assert Hand(
        [
            Card(Colour.CLUBS, Value.TWO),
            Card(Colour.HEARTS, Value.TWO),
            Card(Colour.DIAMONDS, Value.SIX),
            Card(Colour.SPADES, Value.SIX),
            Card(Colour.CLUBS, Value.TEN),
            Card(Colour.HEARTS, Value.QUEEN),
            Card(Colour.DIAMONDS, Value.ACE)
        ]
    ).get_hand_strength() != HandStrength.THREE_OF_A_KIND


def test_is_hand_strength_full_house():
    assert Hand(
        [
            Card(Colour.CLUBS, Value.TWO),
            Card(Colour.HEARTS, Value.TWO),
            Card(Colour.DIAMONDS, Value.TWO),
            Card(Colour.SPADES, Value.SIX),
            Card(Colour.CLUBS, Value.SIX),
            Card(Colour.HEARTS, Value.QUEEN),
            Card(Colour.DIAMONDS, Value.ACE)
        ]
    ).get_hand_strength() == HandStrength.FULL_HOUSE


def test_is_not_hand_strength_full_house():
    assert Hand(
        [
            Card(Colour.CLUBS, Value.TWO),
            Card(Colour.HEARTS, Value.TWO),
            Card(Colour.DIAMONDS, Value.TWO),
            Card(Colour.SPADES, Value.SIX),
            Card(Colour.CLUBS, Value.TEN),
            Card(Colour.HEARTS, Value.QUEEN),
            Card(Colour.DIAMONDS, Value.ACE)
        ]
    ).get_hand_strength() != HandStrength.FULL_HOUSE


def test_is_hand_strength_straight():
    assert Hand(
        [
            Card(Colour.CLUBS, Value.TWO),
            Card(Colour.HEARTS, Value.ACE),
            Card(Colour.DIAMONDS, Value.THREE),
            Card(Colour.SPADES, Value.SIX),
            Card(Colour.CLUBS, Value.FIVE),
            Card(Colour.HEARTS, Value.FOUR),
            Card(Colour.DIAMONDS, Value.ACE)
        ]
    ).get_hand_strength() == HandStrength.STRAIGHT


def test_is_not_hand_strength_straight():
    assert Hand(
        [
            Card(Colour.CLUBS, Value.TWO),
            Card(Colour.HEARTS, Value.TWO),
            Card(Colour.DIAMONDS, Value.TWO),
            Card(Colour.SPADES, Value.SIX),
            Card(Colour.CLUBS, Value.TEN),
            Card(Colour.HEARTS, Value.QUEEN),
            Card(Colour.DIAMONDS, Value.ACE)
        ]
    ).get_hand_strength() != HandStrength.STRAIGHT
