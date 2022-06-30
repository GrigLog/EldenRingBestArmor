import json
from armor_piece import ArmorPiece
import knapsack

unavailable = ['Deathbed Smalls']

def read_pieces():
    with open("armor_data.json", "r") as file:
        json_file = json.load(file)
    pieces = [[], [], [], []]
    for slot in range(4):
        for json_piece in json_file[slot]:
            piece = ArmorPiece.empty()
            piece.__dict__ = json_piece
            if piece.name in unavailable:
                continue
            pieces[slot].append(piece)
    return pieces


def get_value(set: ArmorPiece):
    return set.physical + set.strike + set.slash + set.pierce


def find_best(pieces, weight, value_func):
    weight = int(weight * 10)
    for slot in range(4):
        for p in pieces[slot]:
            for i in range(8):
                p.set_stat(i, p.get_stat(i) * 0.01)
            p.weight = int(p.weight * 10)

    table = knapsack.main(pieces, weight, value_func)

    for slot in range(4):
        for p in pieces[slot]:
            for i in range(8):
                p.set_stat(i, p.get_stat(i) * 100)
            p.weight = p.weight * 0.1

    weights = [round(w * 0.1, 3) for w in range(weight + 1)]
    negations = [round(te.value * 100, 3) for te in table[3]]
    for w in weights:
        print('%5.1f' % w, end='\t')
    print()
    for n in negations:
        print('%5.1f' % n, end='\t')
    print()
    print('%5.3f' % (table[-1][-1].value * 100))
    print('\n'.join([str(e) for e in table[-1][-1].set]))
    print('\n')
    return negations


if __name__ == "__main__":
    pieces = read_pieces()
    weight = float(input("Input weight"))
    n = ArmorPiece.get_number(input("Input stat"))
    value_func = lambda set: set.get_stat(n)
    find_best(pieces.copy(), weight, value_func)
