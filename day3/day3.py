VOLT_SIZE = 12

Memo = dict[int, dict[int, str]]


def solve(input: str) -> int:
    """
    the only special case here is when the largest number is at the end
    """

    c = 0
    for line in input.splitlines():
        # memo[char_idx][remaining_picks] = best value
        memo: Memo = {}
        ans = biggest_subsequence(line, VOLT_SIZE, memo)
        print(f"{line}->{ans}")
        c += int(ans)

    return c


def biggest_subsequence(s: str, picks: int, memo: Memo) -> str:
    if len(s) not in memo:
        memo[len(s)] = {}

    if picks in memo[len(s)]:
        return memo[len(s)][picks]

    if picks == len(s):
        return s

    if not len(s):
        return ""

    if picks == 1:
        return str(max(list(map(lambda x: int(x), s))))

    assert picks <= len(s), (
        f"have less picks than possible, '{s}' remaining with {picks=}"
    )

    best = 0
    for idx in range(len(s) - picks + 1):
        digit = s[idx]
        this = digit + biggest_subsequence(s[idx + 1 :], picks - 1, memo)
        best = max(int(this), int(best))


    b = str(best)
    memo[len(s)][picks] = b
    return b
