import re


def interpret_mapping(mapping: list[str]) -> dict:
    details = re.fullmatch(r"^([a-z]+)-to-([a-z]+) map:$", mapping.pop(0))

    from_type = details.group(1)
    to_type = details.group(2)

    mapping = [x.split(" ") for x in mapping]
    mapping = [list(map(int, m)) for m in mapping]

    return {"from": from_type, "to": to_type, "mapping": mapping}


def convert_range(value: int, ranges: list[list[int]]) -> int:
    for dst_start, src_start, size in ranges:
        if value >= src_start and value < src_start + size:
            return dst_start + (value - src_start)

    # No ranges matched, value is 1:1
    return value


if __name__ == "__main__":
    # Parse the file into something interpretable
    with open("input.txt") as file:
        contents = file.read().strip()

    contents = contents.split("\n\n")

    seed_line = contents.pop(0)

    # Process seed numbers

    the_numbers_mason = seed_line[7:].split(" ")
    seeds = [int(num) for num in the_numbers_mason]

    # Process mappings
    mappings = [interpret_mapping(mapping.split("\n")) for mapping in contents]

    for index, seed in enumerate(seeds):
        for mapping in mappings:
            # Convert from one range to the other
            seeds[index] = convert_range(seeds[index], mapping["mapping"])

    print("Smallest location:", min(seeds))
