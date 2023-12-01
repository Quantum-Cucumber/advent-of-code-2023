import re

start_re = r"^\D*?(one|two|three|four|five|six|seven|eight|nine|zero|\d).*$"
end_re = r"^.*(one|two|three|four|five|six|seven|eight|nine|zero|\d)\D*?$"


def parse_line_words(value: str) -> int:
    value = value.strip()
    head_num = re.fullmatch(start_re, value, re.IGNORECASE)
    tail_num = re.fullmatch(end_re, value, re.IGNORECASE)

    if not head_num or not tail_num:
        print(f"failed on `{value}` - head {head_num} tail {tail_num}")
        exit(1)

    head_num = head_num.group(1)
    tail_num = tail_num.group(1)

    return int(normalise_word_nums(head_num) + normalise_word_nums(tail_num))


def normalise_word_nums(word: str) -> str:
    num_words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }
    return num_words.get(word, word)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    output = 0
    for line in lines:
        output += parse_line_words(line)

    print("Result is: ", output)
