def solve(input: str) -> int:
    problems: list[list[int]] = []
    symbols: list[str] = []

    lines = input.splitlines()

    lines_with_digits = lines[:-1]
    line_with_symbols = lines[-1]

    idx_of_splits: list[int] = []
    for idx, char in enumerate(line_with_symbols):
        if char != " ":
            idx_of_splits.append(idx - 1)
        if char == "*" or char == "+":
            symbols.append(char)
            

    for c in range(len(lines_with_digits[0])):
        problem_idx = (
            next(
                (idx for idx, i in enumerate(idx_of_splits) if i > c),
                len(idx_of_splits),
            )
            - 1
        )

        # skip all blank lines
        if c in idx_of_splits:
            continue

        if problem_idx >= len(problems):
            problems.append([])

        for r in range(len(lines_with_digits)):
            if r == 0:
                problems[problem_idx].append(0)
            
            if lines_with_digits[r][c] == " ":
                continue

            digit = int(lines_with_digits[r][c])

            problems[problem_idx][-1] *= 10
            problems[problem_idx][-1] += digit

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
