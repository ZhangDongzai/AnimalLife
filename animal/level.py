# 等级类
class Level:
    MAX_NUMBER: int = 100       # 最大级数
    UP_EXPERIENCE: int = 50     # 升第1级需要的经验

    def __init__(self) -> None:
        # 创建实例属性
        self.number = 1
        self.experience = 0

    def add(self, experience: int) -> bool:
        # 增加经验
        self.experience += experience

        # 如果: 经验满足升级值 与 当前级数小于最大级数
        if (self.experience >= Level.UP_EXPERIENCE * self.number) and (self.number < Level.MAX_NUMBER):
            
            # 升级并清空经验
            self.experience -= Level.UP_EXPERIENCE * self.number
            self.number += 1

            # 升级返回 True
            return True
        
        else:
            # 未升级返回 False
            return False
        