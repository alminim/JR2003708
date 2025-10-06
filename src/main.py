#!/usr/bin/env python3

##########################
# Dragons and Princesses #
##########################

##### LOGIC #####
# We can "tentatively" kill every dragon we encounter,
# and store them in a priority queue (with their gold being the priority value).
# If we encounter an undesireable princess (not the last princess),
# we can remove the least valuable dragons from the kill list until we have killed less than
# the required number to marry her.
#
# This way, once we pass a princess, we know we have killed less dragons than needed to marry her,
# and all of the dragons we have killed appeared before her. Plus, the dragons we kill will maximize the gold,
# as we will always remove the least valuable dragons.
# Once we reach the last princess, we can easily check if we killed the required number of dragons,
# and if yes how much gold we earn.

from typing import List, Union
import sys
import heapq
from pathlib import Path
from .cell_occupant import Dragon, Princess
from .input_reader import read_input_from_file, validate_input, parse_cells


def solve(cells: List[Union[Dragon, Princess]]) -> List[Dragon]:
    killed_dragons = []

    for i in range(len(cells) - 1):
        cell_occupant = cells[i]
        if type(cell_occupant) is Dragon:
            heapq.heappush(killed_dragons, cell_occupant)
        else:
            while len(killed_dragons) >= cell_occupant.beauty:
                heapq.heappop(killed_dragons)

    if len(killed_dragons) >= cells[-1].beauty:
        return killed_dragons

    return []


def main():
    input_file_name = (
        sys.argv[1] if len(sys.argv) > 1 else "input_files/successful_journey.yaml"
    )
    input_file = Path(input_file_name)
    yaml_data = read_input_from_file(input_file)
    if not validate_input(yaml_data):
        sys.stderr.write("Malformed input!\n")
        sys.exit(-1)

    cells = parse_cells(yaml_data["cells"])
    if not cells:
        sys.stderr.write(
            "Malformed input for cell occupants (dragons and princesses).\n"
        )
        sys.exit(-1)

    killed_dragons = solve(cells)
    if not killed_dragons:
        print("-1")
        return

    total_gold_collected = sum(dragon.gold for dragon in killed_dragons)
    killed_dragons.sort(key=lambda d: d.index)

    print(total_gold_collected)
    print(len(killed_dragons))
    # Add 2 to every index to account for starting to count from 1
    # and the first cell is occupied by the knight
    print(*[dragon.index + 2 for dragon in killed_dragons], sep=" ")


if __name__ == "__main__":
    main()
