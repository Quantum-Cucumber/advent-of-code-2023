# Ngl im mad at this one. The looping thing is wild to figure out.
# Figured out the rough goal of the code because of reddit so Im giving myself only half a star for this

from math import lcm

if __name__ == "__main__":
    with open("input.txt") as file:
        contents = file.read()

    directions, contents = contents.split("\n\n")

    # Process contents
    contents = contents.strip().split("\n")
    mapping = {}
    for line in contents:
        location = line[0:3]
        left = line[7:10]
        right = line[12:15]

        mapping.update({location: {"L": left, "R": right}})

    paths = [[(location, len(directions) - 1)] for location in mapping.keys() if location.endswith("A")]

    for path in paths:
        direction_index = 0
        while 1:
            next_location = mapping[path[-1][0]][directions[direction_index]]

            if (next_location, direction_index) in path:
                break
            else:
                path.append((next_location, direction_index))

            direction_index += 1
            if direction_index == len(directions):
                direction_index = 0

    # Calc cycles and length of each path
    path_stats = []

    for path in paths:
        z_index = None
        for index in range(len(path)):
            if path[index][0].endswith("Z"):
                z_index = index

        path_stats.append(z_index)

    print(lcm(*path_stats))
