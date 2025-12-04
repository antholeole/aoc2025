def solve(input_data: str) -> int:
    ranges_str = input_data.split(",")
    ranges: list[tuple[int, int]] = []

    for r in ranges_str:
        rs = r.split("-")
        ranges.append((int(rs[0]), int(rs[1])))


    sols: set[int] = set()

    for start, end in ranges:
        for v in range(start, end + 1):
            s = str(v)

            midpoint = len(s) // 2
            for end in range(1, midpoint + 1):
                times = (len(s) / end)
                if not times.is_integer():
                    continue

                if s[:end] * int(times) == s:
                    sols.add(v)

    return sum(list(sols))
