# this hsould be a shared util. also make it more optimized
from collections import defaultdict
from heapq import heappop, heappush
from math import sqrt


class UnionFind:
    def __init__(self, total: int):
        self._map: dict[int, int] = {x: x for x in range(total)}

    def union(self, a: int, b: int):
        a_parent = self.find(a)
        b_parent = self.find(b)
        self._map[a_parent] = b_parent

    def find(self, a: int) -> int:
        found = self._map[a]
        if found != a:
            self._map[a] = self.find(found)
            found = self._map[a]
        return found

    def sizes(self) -> list[int]:
        s: dict[int, int] = defaultdict(int)

        for p in self._map.keys():
            s[self.find(p)] += 1

        return list(s.values())


def dist(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    s = 0
    for x, r in zip(a, b):
        s += (x - r) ** 2
    return sqrt(s)


N_SHORTEST = 1000


def solve(input: str) -> int:
    vals: list[tuple[int, int, int]] = []

    for line in input.splitlines():
        a, b, c = line.split(",")
        vals.append((int(a), int(b), int(c)))

    # heap of dist, [a, b]
    min_sizes: list[tuple[float, tuple[int, int]]] = []

    for x in range(len(vals)):
        for r in range(x + 1, len(vals)):
            v = (dist(vals[x], vals[r]), (x, r))
            heappush(min_sizes, v)

    dsu = UnionFind(len(vals))
    for _ in range(N_SHORTEST):
        _, pair = heappop(min_sizes)
        dsu.union(pair[0], pair[1])


    sizes = list(reversed(sorted(dsu.sizes())))

    return sizes[0] * sizes[1] * sizes[2]
