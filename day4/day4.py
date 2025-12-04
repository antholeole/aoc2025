def solve(input: str) -> int:
    grid: list[list[bool]] = []
    for line in input.splitlines():
        grid.append([])
        for v in line:
            grid[-1].append(v == "@")

    def count_surroundings(r: int, c: int) -> int:
        surroundings = 0
        for dc in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                if dr == dc == 0:
                    continue

                if dr + r < 0 or dr + r > len(grid) - 1:
                    continue
                if dc + c < 0 or dc + c > len(grid[0]) - 1:
                    continue

                surroundings += grid[dr + r][dc + c]
        return surroundings

    ans = 0

    while True:
        removed_this_cycle: set[tuple[int, int]] = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    removeable = count_surroundings(r, c) < 4
                    if removeable:
                        removed_this_cycle.add((r, c))
                    ans += removeable

        if not len(removed_this_cycle):
            break

        for r, c in removed_this_cycle:
            grid[r][c] = False
    return ans
