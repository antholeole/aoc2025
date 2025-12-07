def solve(input: str) -> int:
    lines = input.splitlines()

    # from bottom up, if there's a
    possibilties_at_column: dict[int, int] = {x: 1 for x in range(len(lines[0]))}

    for line in reversed(lines[:-1]):
        this_row_possibilties: dict[int, int] = {}
        for c, pos in enumerate(line):
            # if we aren't a splitter, then just carry up the possibilties below
            if pos == ".":
                this_row_possibilties[c] = possibilties_at_column[c]
                continue

            # if we are a splitter, its the possibilities of bottom left and
            # bottom right summed.
            this_row_possibilties[c] = (
                possibilties_at_column[c - 1] + possibilties_at_column[c + 1]
            )
        possibilties_at_column = this_row_possibilties


    # the solution is the number of possibilities at the start point.        
    return possibilties_at_column[lines[0].index('S')]
