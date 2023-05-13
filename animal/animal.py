from level import Level
from propertie import Propertie


# 动物类
class Animal:
    NAME = "Animal"                     # 名称
    PROPERTIM = Propertie()             # 属性

    def __init__(self) -> None:

        # 创建实例属性
        self.level = Level()            # 等级
     