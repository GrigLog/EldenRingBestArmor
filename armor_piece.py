from dataclasses import dataclass


@dataclass(init=True)
class ArmorPiece:
    name: str
    link: str

    physical: float
    strike: float
    slash: float
    pierce: float
    magic: float
    fire: float
    lightning: float
    holy: float

    immunity: int
    robustness: int
    focus: int
    vitality: int

    poise: int

    weight: float

    def get_stat(self, i):
        return [self.physical, self.strike, self.slash, self.pierce, self.magic, self.fire, self.lightning, self.holy, self.immunity, self.robustness, self.focus, self.vitality, self.poise, self.weight][i]

    def set_stat(self, i, value):
        if i == 0:
            self.physical = value
        elif i == 1:
            self.strike = value
        elif i == 2:
            self.slash = value
        elif i == 3:
            self.pierce = value
        elif i == 4:
            self.magic = value
        elif i == 5:
            self.fire = value
        elif i == 6:
            self.lightning = value
        elif i == 7:
            self.holy = value
        elif i == 8:
            self.immunity = value
        elif i == 9:
            self.robustness = value
        elif i == 10:
            self.focus = value
        elif i == 11:
            self.vitality = value
        elif i == 12:
            self.poise = value
        elif i == 13:
            self.weight = value

    @staticmethod
    def empty():
        return ArmorPiece("", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    @staticmethod
    def combine(set):
        return ArmorPiece("",  # ' + '.join([p.name for p in set]),
                          "",
                          1 - (1 - set[0].physical) * (1 - set[1].physical) * (1 - set[2].physical) * (1 - set[3].physical),
                          1 - (1 - set[0].strike) * (1 - set[1].strike) * (1 - set[2].strike) * (1 - set[3].strike),
                          1 - (1 - set[0].slash) * (1 - set[1].slash) * (1 - set[2].slash) * (1 - set[3].slash),
                          1 - (1 - set[0].pierce) * (1 - set[1].pierce) * (1 - set[2].pierce) * (1 - set[3].pierce),
                          1 - (1 - set[0].magic) * (1 - set[1].magic) * (1 - set[2].magic) * (1 - set[3].magic),
                          1 - (1 - set[0].fire) * (1 - set[1].fire) * (1 - set[2].fire) * (1 - set[3].fire),
                          1 - (1 - set[0].lightning) * (1 - set[1].lightning) * (1 - set[2].lightning) * (1 - set[3].lightning),
                          1 - (1 - set[0].holy) * (1 - set[1].holy) * (1 - set[2].holy) * (1 - set[3].holy),
                          set[0].immunity + set[1].immunity + set[2].immunity + set[3].immunity,
                          set[0].robustness + set[1].robustness + set[2].robustness + set[3].robustness,
                          set[0].focus + set[1].focus + set[2].focus + set[3].focus,
                          set[0].vitality + set[1].vitality + set[2].vitality + set[3].vitality,
                          set[0].poise + set[1].poise + set[2].poise + set[3].poise,
                          set[0].weight + set[1].weight + set[2].weight + set[3].weight)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "ArmorPiece(name='{}', link='{}, physical={:.1f}, strike={:.1f}, slash={:.1f}, pierce={:.1f}, magic={:.1f}, fire={:.1f}, lightning={:.1f}, holy={:.1f}, immunity={}, robustness={}, focus={}, vitality={}, poise={}, weight={:.1f})".format(self.name, self.link, self.physical, self.strike, self.slash, self.pierce, self.magic, self.fire, self.lightning, self.holy, self.immunity, self.robustness, self.focus, self.vitality, self.poise, self.weight)



