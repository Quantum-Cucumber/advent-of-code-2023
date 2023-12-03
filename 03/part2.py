# This took 10 minutes sob

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def find_symbols(schematic: list[list[str]]) -> tuple[str, int, int]:
    """Get coords of all symbols in the schematic"""
    for y in range(len(schematic)):
        for x, tile in enumerate(schematic[y]):
            if tile not in NUMBERS + ["."]:
                yield tile, x, y


def find_numbers(schematic: list[list[str]]) -> tuple[int, list[tuple[int, int]]]:
    # Store all the tiles we have checked and that therefore can't be part of any other number
    processed_tiles = []

    for y in range(len(schematic)):
        for x, tile in enumerate(schematic[y]):
            if (x, y) not in processed_tiles and tile in NUMBERS:
                # All the tiles that make up this number
                number = tile
                number_group = [(x, y)]

                # Since we are processing left to right, it should be safe to just check numbers to the right, right?
                # Process all tiles up until the end of the row
                # It took me 1h 25m to debug that this was the issue
                for neighbour_x in range(x + 1, len(schematic[0])):
                    value = schematic[y][neighbour_x]
                    if value in NUMBERS:
                        number += value
                        number_group.append((neighbour_x, y))
                    else:
                        break

                # Add all the tiles that are part of this number, to the exclude list
                processed_tiles += number_group

                # Hooray we have the number
                yield int(number), number_group


def calc_values(numbers: tuple[int, list[tuple[int, int]]],
                symbols: tuple[str, int, int]) -> int:
    result = 0

    for symbol, symbol_x, symbol_y in symbols:
        tiles = tuple(get_adjacent_tiles((symbol_x, symbol_y)))

        if symbol == "*":
            gear_count = 0
            gear_product = 1

            for number, number_coords in numbers:
                if any([tile in number_coords for tile in tiles]):
                    gear_count += 1
                    gear_product *= number

            if gear_count == 2:
                result += gear_product

    return result


def get_adjacent_tiles(tile: tuple[int, int]) -> tuple[tuple[int, int]]:
    """Gets all tiles in a 3x3 area around the tile"""
    for x in range(tile[0] - 1, tile[0] + 2):
        for y in range(tile[1] - 1, tile[1] + 2):
            yield x, y


if __name__ == "__main__":
    with open("input.txt") as file:
        schematic_raw = file.readlines()

    # throw into 2d array

    schematic = [list(line.strip()) for line in schematic_raw]

    # [print(x) for x in schematic]

    symbols = tuple(find_symbols(schematic))
    numbers = tuple(find_numbers(schematic))

    result = calc_values(numbers, symbols)

    print("Result:", result)
