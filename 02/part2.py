from math import prod

def parse_game(game: str) -> iter:
    results = game.split(": ")[1]
    draws = results.split("; ")

    for draw in draws:
        yield parse_draw(draw)


def parse_draw(draw: str) -> dict:
    cubes = draw.split(", ")

    # Grab all specified values and put them into {colour: count}
    draw_dict = {}
    for cubes in cubes:
        count, colour = cubes.split(" ")
        draw_dict.update({colour: int(count)})

    return draw_dict


def min_cubes_needed_for_game(game: iter) -> dict:
    min_count = {"red": 0, "green": 0, "blue": 0}

    for draw in game:
        # Check if this draw would have needed any more cubes than the current minimum
        for colour, count in min_count.items():
            if draw.get(colour, 0) > count:
                min_count[colour] = draw[colour]

    return min_count


if __name__ == "__main__":
    # Load the text file
    with open("input.txt") as file:
        input_lines = file.readlines()

    # Parse out the raw strings into usable data

    parsed_lines = []
    for line in input_lines:
        parsed_lines.append(parse_game(line.strip()))

    min_counts = []
    for game in parsed_lines:
        min_counts.append(min_cubes_needed_for_game(game))

    powers = [prod(cubes.values()) for cubes in min_counts]
    result = sum(powers)

    print("Magic number is", result)
