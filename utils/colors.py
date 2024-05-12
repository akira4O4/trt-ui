from dataclasses import dataclass


@dataclass
# RGB
class Colors:
    RED: tuple = (255, 0, 0)
    GREED: tuple = (0, 255, 0)
    BLUE: tuple = (0, 0, 255)
    KleinBlue: tuple = (0, 47, 167)
    PeacockBlue: tuple = (73, 148, 196)  # 孔雀蓝
    MarsGreen: tuple = (1, 132, 127)
    ChinaRed: tuple = (230, 0, 0)
    BurgundyRed: tuple = (144, 0, 33),
    BiShanGreen: tuple = (119, 150, 73)  # 碧山
