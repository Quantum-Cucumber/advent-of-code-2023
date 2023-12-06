# Brute force babey
# A speedy 1h40min run time.
# I can imagine better ways to do that but my brain was more willing to wait than to think

import re
from math import inf
from time import time


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
    start_time = time()

    # Parse the file into something interpretable
    with open("test_input.txt") as file:
        contents = file.read().strip()

    contents = contents.split("\n\n")

    seed_line = contents.pop(0)

    # Process seed numbers

    the_numbers_mason = seed_line[7:].split(" ")
    seeds = [int(num) for num in the_numbers_mason]

    # Process mappings
    mappings = [interpret_mapping(mapping.split("\n")) for mapping in contents]

    # store a single value between runs. We only care about whether the value computed is lower than the previous lowest
    smallest_value = inf
    # Iterate through the seed numbers. Skip every second since the numbers are now in pairs
    for seed_index in range(0, len(seeds), 2):
        start = seeds[seed_index]
        size = seeds[seed_index + 1]

        # This is the awful bit. Go through every seed in the range
        for seed in range(start, start + size):
            # initialise value to store the current value taken from the mappings as we iterate
            value = seed
            for mapping in mappings:
                # Convert from one range to the other
                value = convert_range(value, mapping["mapping"])

            # Work out if the new value is the current smallest value
            smallest_value = min(smallest_value, value)

        print("Range completed in", time() - start_time)

    print("Smallest location:", smallest_value)
    print("This took", time() - start_time, "s")
