def solve(input_data: str) -> int:
    ranges_str = input_data.split(",")
    ranges: list[tuple[int, int]] = []

    for r in ranges_str:
        rs = r.split("-")
        ranges.append((int(rs[0]), int(rs[1])))


    c = 0

    for start, end in ranges:
        for v in range(start, end + 1):
            s = str(v)
            if len(s) % 2 != 0:
                continue

            midpoint = len(s) // 2
            first_half = s[:midpoint]

            if first_half * 2 == s:
                c += v


    return c
