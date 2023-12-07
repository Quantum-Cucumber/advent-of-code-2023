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


def card_to_value(card: str) -> int:
    # Convert letters to ints
    if card.isdigit():
        return int(card)
    elif card == "T":
        return 10
    elif card == "J":
        return 11
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.type = self.determine_type()

    def determine_type(self) -> HandType:
        # The only thing that matters here is the count of each card. The card itself and the order is irrelevant
        unique_cards = set(self.cards)
        counts = []
        for card in unique_cards:
            counts.append(self.cards.count(card))

        # Sort from highest to lowest to make pattern matching easier
        counts = sorted(counts, reverse=True)
        counts = "".join(map(str, counts))

        return HAND_MAPPING[counts]

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

    print("Total scores:", total_scores)
