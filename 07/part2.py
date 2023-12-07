from enum import IntEnum


class HandType(IntEnum):
    FIVE_KIND = 6
    FOUR_KIND = 5
    FULL_HOUSE = 4
    THREE_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


# Maps a count of unique cards in a hand to the actual hand type
HAND_MAPPING = {
    "5": HandType.FIVE_KIND,
    "41": HandType.FOUR_KIND,
    "32": HandType.FULL_HOUSE,
    "311": HandType.THREE_KIND,
    "221": HandType.TWO_PAIR,
    "2111": HandType.ONE_PAIR,
    "11111": HandType.HIGH_CARD,
}
# How hand mappings will be upgraded with one J card
HAND_UPGRADES = {
    # 5 -> 5
    HandType.FIVE_KIND: HandType.FIVE_KIND,
    # 4 1 -> 5
    HandType.FOUR_KIND: HandType.FIVE_KIND,
    # 3 2 -> 4 1
    HandType.FULL_HOUSE: HandType.FOUR_KIND,
    # 3 1 1 -> 4 1 1
    HandType.THREE_KIND: HandType.FOUR_KIND,
    # 2 2 1 -> 3 2
    HandType.TWO_PAIR: HandType.FULL_HOUSE,
    # 2 1 1 1 -> 3 1 1 1
    HandType.ONE_PAIR: HandType.THREE_KIND,
    # 1 1 1 1 1 -> 2 1 1 1
    HandType.HIGH_CARD: HandType.ONE_PAIR,
}


def card_to_value(card: str) -> int:
    # Convert letters to ints
    if card.isdigit():
        return int(card)
    elif card == "T":
        return 10
    elif card == "J":
        return 1
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14


class Hand:
    def __init__(self, cards: list[int], bid: int):
        self.cards = cards
        self.bid = bid
        self.type = self.determine_type()

    def determine_type(self) -> HandType:
        # 'J's need to turn into other random values for the sake of counting duplicates
        # Otherwise if theres more than 3, the bad upgrades will be bad

        cards = []
        for offset, card in enumerate(self.cards):
            if card == 1:
                # This is a very lazy effort. It just needs to be unique lol
                cards.append(100 + offset)
            else:
                cards.append(card)

        unique_cards = set(cards)
        counts = {}
        for card in unique_cards:
            counts.update({card: cards.count(card)})

        # Sort from highest to lowest to make pattern matching easier
        counts = sorted(counts.values(), reverse=True)
        counts = "".join(map(str, counts))

        result = HAND_MAPPING[counts]

        # For each J, upgrade the type of the card
        for _ in range(self.cards.count(1)):
            result = HAND_UPGRADES[result]

        return result

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        else:
            for i in range(5):
                # If the values are equal, check the next, otherwise return the result
                if self.cards[i] != other.cards[i]:
                    return self.cards[i] < other.cards[i]

    def __gt__(self, other):
        if self.type != other.type:
            return self.type > other.type
        else:
            for i in range(5):
                if self.cards[i] != other.cards[i]:
                    return self.cards[i] > other.cards[i]


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    # load into usable thing
    hands = []
    for line in lines:
        cards, bid = line.strip().split(" ")
        cards = list(map(card_to_value, cards))

        hand = Hand(cards, int(bid))

        hands.append(Hand(cards, int(bid)))

    hands = sorted(hands)

    total_scores = 0
    for index, hand in enumerate(hands):
        total_scores += (index + 1) * hand.bid

        print(hand.cards, hand.type)

    print("Total scores:", total_scores)
