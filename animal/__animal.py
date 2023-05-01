class Propertie:
    name: str
    restrained_properties: list


class Level:
    MAX_NUMBER: int
    UP_EXPERIENCE: int

    def __init__(self) -> None:
        self.number = 1
        self.experience = 0

    def add(self, experience: int) -> None:
        self.experience += experience

        # 如果: 经验满足升级值 与 当前级数小于最大级数 则 升级并清空经验
        if (self.experience >= Level.UP_EXPERIENCE * self.number) and (self.number < Level.MAX_NUMBER):
            self.experience -= Level.UP_EXPERIENCE * self.number
            self.number += 1

        
class Animal:
    name: str
    propertie: Propertie

    def __init__(self) -> None:
        self.level = Level()
        