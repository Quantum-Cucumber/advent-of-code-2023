# This took me 4h 45min .-.
# Also this code is very bad i got quite frustrated

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def get_symbol_positions(schematic: list[list[str]]) -> iter:
    """Get coords of all symbols in the schematic"""
    for y in range(len(schematic)):
        for x, tile in enumerate(schematic[y]):
            if tile not in NUMBERS + ["."]:
                yield x, y


def find_numbers(schematic: list[list[str]]) -> tuple[int, list[tuple[int, int]]]:
    # Store all the tiles we have checked and that therefore can't be part of any other number
    processed_tiles = []

    for y in range(len(schematic)):
        for x, tile in enumerate(schematic[y]):
            if (x, y) not in processed_tiles and tile in NUMBERS:
                # All the tiles that make up this number
                number = tile
                number_group = [(x, y)]

                print("finding for", x)
                # Since we are processing left to right, it should be safe to just check numbers to the right, right?
                # Process all tiles up until the end of the row
                # It took me 1h 25m to debug that this was the issue
                for neighbour_x in range(x + 1, len(schematic[0])):
                    print(neighbour_x)
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


#This one allows for duplicate part numbers
# def numbers_with_adjacency(numbers: tuple[int, list[tuple[int, int]]],
#                            symbol_coords: tuple[tuple[int, int]]) -> list[int]:
#     for part in symbol_coords:
#         tiles = tuple(get_adjacent_tiles(part))
#
#         for number, number_coords in numbers:
#             if any([tile in number_coords for tile in tiles]):
#                 yield number

def numbers_with_adjacency(numbers: tuple[int, list[tuple[int, int]]],
                           symbol_coords: tuple[tuple[int, int]]) -> list[int]:
    eligible_tiles = []
    for tile in symbol_coords:
        eligible_tiles += get_adjacent_tiles(tile)

    for number, number_coords in numbers:
        if any([coord in number_coords for coord in eligible_tiles]):
            print(number)
            yield number


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

    symbol_coords = tuple(get_symbol_positions(schematic))
    numbers = tuple(find_numbers(schematic))

    part_numbers = tuple(numbers_with_adjacency(numbers, symbol_coords))
    print(len(part_numbers))

    print("Sum of part numbers =", sum(part_numbers))
