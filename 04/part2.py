def process_cards(line: str) -> tuple[list[int], list[int]]:
    # Strip card info
    line = line.strip().split(": ")[1]

    winning_nums, card_nums = line.split(" | ")
    winning_nums = [int(x) for x in winning_nums.split(" ") if x]
    card_nums = [int(x) for x in card_nums.split(" ") if x]

    return winning_nums, card_nums


def match_winning_numbers(winning_nums, card_nums) -> list[int]:
    return [num for num in card_nums if num in winning_nums]


if __name__ == "__main__":
    # Load the text file
    with open("input.txt") as file:
        input_lines = file.readlines()

    cards = map(process_cards, input_lines)

    # Calc number of matches per card
    wins = []
    for win_nums, card_nums in cards:
        wins.append(len(match_winning_numbers(win_nums, card_nums)))
    card_counts = [[count, 1] for count in wins]

    for index, (value, copies) in enumerate(card_counts):
        # Copy the next [value] cards
        for i in range(index + 1, index + value + 1):
            card_counts[i][1] += 1 * copies

    print(card_counts)

    result = sum([x[1] for x in card_counts])
    print(result)
