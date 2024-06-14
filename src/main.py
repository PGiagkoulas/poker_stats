from enum import Enum
from collections import Counter
import operator


class Colour(Enum):
    SPADES = 1
    CLUBS = 2
    HEARTS = 3
    DIAMONDS = 4


class Value(Enum):
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 7
    NINE = 8
    TEN = 9
    JACK = 10
    QUEEN = 11
    KING = 12
    ACE = 13


class HandStrength(Enum):
    ROYAL_FLUSH = 1
    STRAIGHT_FLUSH = 2
    FOUR_OF_A_KIND = 3
    FULL_HOUSE = 4
    FLUSH = 5
    STRAIGHT = 6
    THREE_OF_A_KIND = 7
    TWO_PAIR = 8
    ONE_PAIR = 9
    HIGH_CARD = 10


class Card:
    colour: Colour
    value: Value

    def __init__(self, c: Colour, v: Value):
        self.colour = c
        self.value = v

    def __str__(self):
        return self.value.name + " of " + self.colour.name

    def __eq__(self, other):
        return self.value.value == other.value.value

    def __le__(self, other):
        return self.value.value <= other.value.value

    def __lt__(self, other):
        return self.value.value < other.value.value

    def __ge__(self, other):
        return self.value.value >= other.value.value

    def __gt__(self, other):
        return self.value.value > other.value.value


class Hand:
    cards: list[Card]

    def __init__(self, drawn_cards: list[Card]):
        self.cards = drawn_cards

    def __str__(self):
        return " | ".join([str(c) for c in self.cards])

    def __create_counter_dict(self, colour_or_value) -> Counter:
        """
        Helper function to generate a dictionary of counts. It is intended to be applied on Card objects, for either
        counting instances of colours or values.

        :param colour_or_value: selecting either colour or value of Cards to count instances
        :return: the Counter based on colour_value selection
        """
        return Counter([operator.attrgetter(colour_or_value)(c) for c in self.cards])

    def __is_full_house(self) -> bool:
        """
        Function that checks if FULL_HOUSE is the strongest combination of cards in a given hand.

        :return: True, if exactly 1 triplet and 1 pair are present, False otherwise
        """
        if self.__is_three_of_a_kind() and self.__is_one_pair():
            return True
        return False

    def __is_flush(self) -> bool:
        """
        Function that checks if FLUSH is the strongest combination of cards in a given hand.

        :return: True, if at least 5 cards of the same colour are in the hand, False otherwise
        """
        counter_dict = self.__create_counter_dict("colour")
        if any(count >= 5 for count in counter_dict.values()):
            return True
        return False

    def __is_straight(self) -> bool:
        """
        Function that checks if STRAIGHT is the strongest combination of cards in a given hand.

        :return: True, if , False otherwise
        """
        sorted_card_values = [c.value.value for c in self.cards]
        sorted_card_values.sort()
        card_value_diffs = [(sorted_card_values[i+1] - sorted_card_values[i]) % 12
                            for i in range(len(sorted_card_values) - 1)]
        if sum(1 for diff in card_value_diffs if diff == 1) >= 4:  # TODO: detect straight start & end
            return True
        return False

    def __is_three_of_a_kind(self) -> bool:
        """
        Function that checks if THREE_OF_A_KIND is the strongest combination of cards in a given hand.

        :return: True, if exactly 1 triplet with the same value is present, False otherwise
        """
        counter_dict = self.__create_counter_dict("value")
        if sum(1 for count in counter_dict.values() if count == 3) == 1:
            return True
        return False

    def __is_two_pair(self) -> bool:
        """
        Function that checks if TWO_PAIR is the strongest combination of cards in a given hand.

        :return: True, if exactly 2 pairs with the same value are present, False otherwise
        """
        counter_dict = self.__create_counter_dict("value")
        if sum(1 for count in counter_dict.values() if count == 2) == 2:
            return True
        return False

    def __is_one_pair(self) -> bool:
        """
        Function that checks if ONE_PAIR is the strongest combination of cards in a given hand.

        :return: True, if exactly 1 pair with the same value is present, False otherwise
        """
        counter_dict = self.__create_counter_dict("value")
        if sum(1 for count in counter_dict.values() if count == 2) == 1:
            return True
        return False

    def get_hand_strength(self) -> HandStrength:
        """
        Function that calculates the strength of a given hand.
        :return: HandStrength calculated
        """
        hand_strength = HandStrength.HIGH_CARD
        if self.__is_full_house():
            hand_strength = HandStrength.FULL_HOUSE
        elif self.__is_flush():
            hand_strength = HandStrength.FLUSH
        elif self.__is_straight():
            hand_strength = HandStrength.STRAIGHT
        elif self.__is_three_of_a_kind():
            hand_strength = HandStrength.THREE_OF_A_KIND
        elif self.__is_two_pair():
            hand_strength = HandStrength.TWO_PAIR
        elif self.__is_one_pair():
            hand_strength = HandStrength.ONE_PAIR
        return hand_strength


if __name__ == '__main__':
    my_hand = Hand(
        [
            Card(Colour.CLUBS, Value.TWO),
            Card(Colour.HEARTS, Value.ACE),
            Card(Colour.DIAMONDS, Value.THREE),
            Card(Colour.SPADES, Value.SIX),
            Card(Colour.CLUBS, Value.FIVE),
            Card(Colour.HEARTS, Value.FOUR),
            Card(Colour.DIAMONDS, Value.ACE)
        ]
    )
    print(my_hand)
    print(my_hand.get_hand_strength())
