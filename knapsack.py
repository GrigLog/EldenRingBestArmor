from dataclasses import dataclass
from armor_piece import ArmorPiece

@dataclass
class ArmorTest:
    weight:int
    defense:int

    @staticmethod
    def empty():
        return ArmorTest(0, 0)

    @staticmethod
    def combine(set):
        return ArmorTest(set[0].weight + set[1].weight + set[2].weight + set[3].weight,
                         set[0].defense + set[1].defense + set[2].defense + set[3].defense)


class TableEntry:
    value_func = lambda set: 0

    def __init__(self, set=None):
        if set is None:
            set = [ArmorPiece.empty() for i in range(4)]
        self.set = set
        self.value = TableEntry.value_func(ArmorPiece.combine(set))

    def withPiece(self, armor, slot):
        set = self.set.copy()
        set[slot] = armor
        te = TableEntry(set)
        return te

    def __repr__(self):
        return '{' + str(self.value) + '}'


def main(pieces, weight, value_func):
    TableEntry.value_func = value_func
    table = [[TableEntry() for i in range(weight + 1)] for s in range(4)]
    for slot in range(4):
        for w in range(0, weight + 1):
            mx = table[slot - 1][w] if slot - 1 >= 0 else TableEntry()
            for p in pieces[slot]:
                if w - p.weight >= 0:
                    if slot-1 >= 0:
                        te = table[slot-1][w-p.weight].withPiece(p, slot)
                    else:
                        te = TableEntry().withPiece(p, slot)
                    if te.value > mx.value:
                        mx = te
                table[slot][w] = mx
    return table


if __name__ == "__main__":
    pieces = [[ArmorTest(1, 5), ArmorTest(2, 7)],
              [ArmorTest(3, 8), ArmorTest(4, 10), ArmorTest(6, 16)],
              [ArmorTest(2, 1), ArmorTest(3, 3)],
              [ArmorTest(2, 4), ArmorTest(3, 5), ArmorTest(4, 6)]]
    weight = 10
    main(pieces, weight, value_func=lambda set: set.defense)