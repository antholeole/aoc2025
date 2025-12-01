def solve(input_data: str)-> int:
    count_zero = 0
    at = 50

    for line in input_data.split("\n"):
        dir = -1 if line[0] == "L" else 1
        raw_turns = int(line[1:]) * dir

        passes, at_ = divmod(raw_turns + at, 100)

        # "trivial" passes
        count_zero += abs(passes)

        # testcase "R50,L1" reveals this edge case. Starting at 0 and going left
        # gives a false value because e.g. -88 // 100 = 1, but we never passed
        # 0.
        if at == 0 and dir == -1:
            count_zero -= 1

        # testcase "L50" reveals this condition. if you end up at 0 from a left pass,
        # you need to count it. Right passes that end a 0 (100, 200) get counted
        # properly.
        if at_ == 0 and dir == -1:
            count_zero += 1

        at = at_

    return count_zero
