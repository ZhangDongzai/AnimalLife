from level import Level
from propertie import Propertie


# 动物类
class Animal:
    NAME = "Animal"             # 名称
    PROPERTIM = Propertie()     # 属性

    def __init__(self) -> None:

        # 创建实例属性
        self.level = Level()    # 等级
    

if __name__ == "__main__":
    animal = Animal()

    text = """\
This is an animal object.
Its name is {name}.
Its propertie is {propertie_name}.
Its level's number is {level_number}.\
    """.format(
        name=animal.NAME, 
        propertie_name=animal.PROPERTIM.NAME, 
        level_number=animal.level.number)
    
    print(text)
