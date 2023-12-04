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

    score = 0

    for winning_nums, card_nums in cards:
        wins = match_winning_numbers(winning_nums, card_nums)
        print(wins)

        if wins:
            score += 2 ** (len(wins) - 1)
            print(2 ** (len(wins) - 1))

    print("Score is:", score)
