from collections import namedtuple

Coord = namedtuple("Coordinate", "x y")

GALAXY = "#"
EMPTY = "."
EMPTY_MULTIPLIER = 1_000_000


def find_empty_rows(grid: list[list[str]]) -> iter:
    for y_index, y in enumerate(grid):
        if all([x == EMPTY for x in y]):
            yield y_index


def find_empty_columns(grid: list[list[str]]) -> iter:
    for x_index in range(len(grid[0])):
        galaxies = False
        for y_index in range(len(grid)):
            if grid[y_index][x_index] == GALAXY:
                galaxies = True
                break

        if not galaxies:
            yield x_index


def print_grid(grid: list[list[str]]) -> None:
    # ^ Debug thing
    for y in grid:
        print("".join(y))


def find_galaxies(grid: list[list[str]]) -> list[Coord]:
    for y_index, y in enumerate(grid):
        for x_index, x in enumerate(y):
            if x == GALAXY:
                yield Coord(x_index, y_index)


def get_len(coord_a: Coord, coord_b: Coord, rows: list[int], cols: list[int]) -> int:
    smallest_x = min(coord_a.x, coord_b.x)
    largest_x = max(coord_a.x, coord_b.x)

    smallest_y = min(coord_a.y, coord_b.y)
    largest_y = max(coord_a.y, coord_b.y)

    additional_rows = len([row for row in rows if smallest_y < row < largest_y])
    additional_cols = len([col for col in cols if smallest_x < col < largest_x])

    # -1 because largest-smallest counts each row/col once
    return (additional_rows + additional_cols) * (EMPTY_MULTIPLIER - 1) + (largest_y - smallest_y) + (largest_x - smallest_x)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    grid = [list(line.strip()) for line in lines]

    galaxy_coords = list(find_galaxies(grid))
    empty_rows = list(find_empty_rows(grid))
    empty_columns = list(find_empty_columns(grid))

    total_lengths = 0
    for index_a, coord_a in enumerate(galaxy_coords):
        for index_b in range(index_a, len(galaxy_coords)):
            coord_b = galaxy_coords[index_b]

            total_lengths += get_len(coord_a, coord_b, empty_rows, empty_columns)

    print("Total:", total_lengths)
