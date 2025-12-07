def solve(input: str) -> int:
    beams_split = 0

    lines = input.splitlines()
    prev_row_beams: set[int] = {lines[0].index("S")}

    for line in lines[1:]:
        this_row_beams: set[int] = set()
        for c, pos in enumerate(line):
            # if there's no beam above us we can't do anything
            if c not in prev_row_beams:
                continue

            if pos == "^":
                this_row_beams.add(c - 1)
                this_row_beams.add(c + 1)
                beams_split += 1
            else:
                this_row_beams.add(c)
        prev_row_beams = this_row_beams
    return beams_split
