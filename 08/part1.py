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

    steps = 1
    direction_index = 0
    location = "AAA"
    while location != "ZZZ":
        location = mapping[location][directions[direction_index]]

        if location == "ZZZ":
            break
        else:
            steps += 1

        direction_index += 1
        if direction_index == len(directions):
            direction_index = 0

    print("AAA to ZZZ took", steps, "steps")
