from level import Level
from propertie import Propertie


# 动物类
class Animal:
    NAME: str = "Animal"                    # 名称
    PROPERTIM: Propertie = Propertie()      # 属性

    def __init__(self) -> None:
        # 创建实例属性

        ## 共有(复制)
        self.NAME = Animal.NAME             # 名称    
        self.PROPERTIM = Animal.PROPERTIM   # 属性

        ## 私有(创建)
        self.level = Level()                # 等级
        