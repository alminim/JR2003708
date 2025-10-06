from dataclasses import dataclass, field


@dataclass(order=True)
class Dragon:
    gold: int
    index: int = field(compare=False)


@dataclass
class Princess:
    beauty: int
    index: int
