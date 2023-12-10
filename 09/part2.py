def compute_deltas(history: list[int]) -> list[list[int]]:
    deltas = [history]

    # while so that we can loop dynamically
    while True:
        row = deltas[-1]
        new_row = []

        for i in range(len(row) - 1):
            new_row.append(row[i+1] - row[i])

        deltas.append(new_row)

        if all([value == 0 for value in new_row]):
            return deltas


def calc_next(deltas: list[list[int]]) -> int:
    value = 0
    for delta_index in range(len(deltas) - 2, -1, -1):
        value = deltas[delta_index][0] - value

    return value


if __name__ == "__main__":
    with open("input.txt") as file:
        histories = file.readlines()

    histories = [list(map(int, history.split(" "))) for history in histories]

    total = 0
    for history in histories:
        deltas = compute_deltas(history)
        total += calc_next(deltas)

    print("Total:", total)
