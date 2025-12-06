def solve(input: str) -> int:
    problems: list[list[int]] = []
    symbols: list[str] = []

    num_problems = len(input.splitlines()[0].split())
    for _ in range(num_problems):
        problems.append([])

    for line in input.splitlines():
        line_clean = " ".join(line.split())
        for idx, val in enumerate(line_clean.split(" ")):
            if val == "*" or val == "+":
                symbols.append(val)
            else:
                problems[idx].append(int(val))

    total = 0
    for idx, problem in enumerate(problems):
        current = 0
        if symbols[idx] == "*":
            current = 1

        def apply(v: int) -> int:
            return current * v if symbols[idx] == "*" else current + v

        for digit in problem:
            current = apply(digit)

        total += current

    return total
