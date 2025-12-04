

def solve(input: str) -> int:
    """
    the only special case here is when the largest number is at the end
    """

    c = 0
    for line in input.splitlines():
        high = 0
        for a in range(len(line)):
            for b in range(a + 1, len(line)):
                high = max(high, int(f"{line[a]}{line[b]}"))
        c += high

    return c
