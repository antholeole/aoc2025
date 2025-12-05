def solve(input: str) -> int:
    ingredients: list[int] = []
    ranges: list[tuple[int, int]] = []
    blank = False
    for line in input.splitlines():
        if line == "":
            blank = True
            continue

        if blank:
            ingredients.append(int(line))
        else:
            parts = line.split("-")
            ranges.append((int(parts[0]), int(parts[1])))

    fresh = 0
    for ingredient in ingredients:
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh += 1

        
    
    return fresh
