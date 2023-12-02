CUBE_LIMIT = {
    "red": 12,
    "green": 13,
    "blue": 14
}


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


def is_game_possible(game: iter):
    # Validate each draw in the game
    for draw in game:
        # Check each colour against the
        for colour, count in CUBE_LIMIT.items():
            if draw.get(colour, 0) > count:
                return False

    return True


if __name__ == "__main__":
    # Load the text file
    with open("input.txt") as file:
        input_lines = file.readlines()

    # Parse out the raw strings into usable data

    parsed_lines = []
    for line in input_lines:
        parsed_lines.append(parse_game(line.strip()))

    # Process which games were possible and get the total of the game #s

    total = 0

    # Check each game
    for game_index, game in enumerate(parsed_lines):
        if is_game_possible(game):
            total += game_index + 1

    print("Result is", total)
