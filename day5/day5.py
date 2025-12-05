def solve(input: str) -> int:
    ranges: list[tuple[int, int]] = []
    for line in input.splitlines():
        if line == "":
            break

        parts = line.split("-")
        ranges.append((int(parts[0]), int(parts[1])))

    ranges.sort(key = lambda r: r[0])
    ranges_overlapped: list[tuple[int, int]] = []
    currstart = ranges[0][0]
    currend = ranges[0][1]
    for start, end in ranges[1:]:
        if start <= currend:
            currend = max(currend, end)
        else:
            ranges_overlapped.append((currstart, currend))
            currstart = start
            currend = end
    ranges_overlapped.append((currstart, currend))

    fresh = 0
    for start, end in ranges_overlapped:
        fresh += end - start + 1
    
    return fresh
