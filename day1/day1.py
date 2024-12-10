def solve(input_data: str)-> int:
    count_zero = 0
    at = 50

    for line in input_data.split("\n"):
        dir = -1 if line[0] == "L" else 1
        
        raw_turns = int(line[1:]) * dir
        at += raw_turns
        at %= 100

        if at == 0:
            count_zero += 1

    return count_zero
