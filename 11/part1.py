from collections import namedtuple

Coord = namedtuple("Coordinate", "x y")

GALAXY = "#"
EMPTY = "."


def expand_grid(grid: list[list[str]]) -> None:
    expand_columns(grid)
    expand_rows(grid)


def expand_rows(grid: list[list[str]]) -> None:
    # Find empty rows
    rows = []

    for y_index, y in enumerate(grid):
        if all([x == EMPTY for x in y]):
            rows.append(y_index)

    # Add rows
    # Reverse rows so that higher values don't need to be offset to account for insertions
    for row_index in rows[::-1]:
        grid.insert(row_index, [EMPTY] * len(grid[0]))


def expand_columns(grid: list[list[str]]) -> None:
    # Find empty columns
    columns = []

    for x_index in range(len(grid[0])):
        galaxies = False
        for y_index in range(len(grid)):
            if grid[y_index][x_index] == GALAXY:
                galaxies = True
                break

        if not galaxies:
            columns.append(x_index)

    # Add columns
    for column_index in columns[::-1]:
        for y in grid:
            y.insert(column_index, EMPTY)


def print_grid(grid: list[list[str]]) -> None:
    # ^ Debug thing
    for y in grid:
        print("".join(y))


def find_galaxies(grid: list[list[str]]) -> list[Coord]:
    for y_index, y in enumerate(grid):
        for x_index, x in enumerate(y):
            if x == GALAXY:
                yield Coord(x_index, y_index)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    grid = [list(line.strip()) for line in lines]
    expand_grid(grid)

    galaxy_coords = list(find_galaxies(grid))

    total_lengths = 0
    for index_a, coord_a in enumerate(galaxy_coords):
        for index_b in range(index_a, len(galaxy_coords)):
            coord_b = galaxy_coords[index_b]
            total_lengths += abs(coord_a.x - coord_b.x) + abs(coord_a.y - coord_b.y)

    print("Total:", total_lengths)
