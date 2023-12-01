nums = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


def parse_line_digits(value: str) -> int:
    head_num = None
    tail_num = None

    for char in value:
        if char in nums:
            head_num = char
            break

    for char in value[::-1]:
        if char in nums:
            tail_num = char
            break

    if head_num is None or tail_num is None:
        print(f"failed on `{value}` - head {head_num} tail {tail_num}")
        exit(1)

    return int(head_num + tail_num)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    output = 0
    for line in lines:
        output += parse_line_digits(line)

    print("Result is: ", output)
