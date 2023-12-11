from collections import namedtuple
from math import ceil

Coord = namedtuple("Coord", "x y")

NORTH = Coord(0, -1)
EAST = Coord(1, 0)
SOUTH = Coord(0, 1)
WEST = Coord(-1, 0)

PIPES = {
    "|": (NORTH, SOUTH),
    "-": (WEST, EAST),
    "F": (EAST, SOUTH),
    "7": (WEST, SOUTH),
    "L": (NORTH, EAST),
    "J": (NORTH, WEST),
}

OPPOSITES = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    EAST: WEST,
    WEST: EAST,
}


def coord_on_grid(grid: list[list[str]], coord: Coord) -> bool:
    """Return true if coordinate is in the bounds of the grid"""
    return 0 <= coord.x < len(grid[0]) and 0 <= coord.y < len(grid)


def find_s(grid: list[list[str]]) -> Coord:
    for y_index, y in enumerate(grid):
        for x_index, x in enumerate(y):
            if x == "S":
                return Coord(x_index, y_index)


def find_s_direction(grid: list[list[str]], s_coord: Coord) -> Coord:
    """Find a singular connection to x"""
    # Loop through each pairing of opposites
    for direction, opposite in OPPOSITES.items():
        # Find the tile in that direction
        # Account for edges
        if not coord_on_grid(grid, Coord(s_coord.x + direction.x, s_coord.y + direction.y)):
            continue

        tile = grid[s_coord.y + direction.y][s_coord.x + direction.x]

        # Work out what connections that pipe has
        if tile in PIPES:
            connections = PIPES[tile]
            # If that pipe has a connection faces back to this tile
            if opposite in connections:
                return direction


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    grid = [list(line.strip()) for line in lines]

    start_coord = find_s(grid)

    current_tile = start_coord
    visited_tiles = [current_tile]
    travel_dir = find_s_direction(grid, start_coord)
    while True:
        # Travel in the given direction
        current_tile = Coord(current_tile.x + travel_dir.x, current_tile.y + travel_dir.y)
        # Check if tile has been travelled to and exit instead
        if current_tile in visited_tiles:
            break
        # Add tile to list
        else:
            visited_tiles.append(current_tile)

        # Work out the direction to travel in next (this step is here purely for find_s_direction to be already calculated)
        pipe = grid[current_tile.y][current_tile.x]
        possible_directions = PIPES[pipe]
        for possible_direction in possible_directions:
            # If the opposite of that direction is the direction we travelled in, that will take us back to the old tile
            if travel_dir != OPPOSITES[possible_direction]:
                travel_dir = possible_direction
                break

    print("Furthest steps:", ceil(len(visited_tiles) / 2))

