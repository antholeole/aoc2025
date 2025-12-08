# this hsould be a shared util. also make it more optimized
from collections import defaultdict
from heapq import heappop, heappush
from math import sqrt


class UnionFind:
    def __init__(self, total: int):
        self._map: dict[int, int] = {x: x for x in range(total)}
        self._sizes: dict[int, int] ={x: 1 for x in range(total)}

    def union(self, a: int, b: int):
        a_parent = self.find(a)
        b_parent = self.find(b)

        if a_parent == b_parent:
            return

        # join with bigger parent, update size
        if self._sizes[a_parent] < self._sizes[b_parent]:
            self._map[a_parent] = b_parent
            self._sizes[b_parent] += self._sizes[a_parent]
        else:
            self._map[b_parent] = a_parent
            self._sizes[a_parent] += self._sizes[b_parent]

    def size_of(self, a: int) -> int:
        return self._sizes[self.find(a)]

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
    while len(min_sizes):
        _, pair = heappop(min_sizes)
        dsu.union(pair[0], pair[1])
        if dsu.size_of(pair[0]) >= len(vals):
            return vals[pair[0]][0] * vals[pair[1]][0]

    assert False, "should have connected everything at some point"



