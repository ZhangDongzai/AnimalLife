# 属性类
class Propertie:
    NAME = "propertie"           # 名称
    RESTRAINED_PROPERTIE = ""    # 克制
    DISSOLVE_PROPERTIE = []      # 融合

    # BUFF
    ATTACK = 0                  # 攻击
    DEFENSE = 0                 # 防御
    VITALITY = 0                # 生命


"""
相生: 金生水, 水生木, 木生火, 火生土, 土生金
相克: 金克木, 木克土, 土克水, 水克火, 火克金
"""
class Gold(Propertie):
    NAME = "金"
    RESTRAINED_PROPERTIE = "木"
    DISSOLVE_PROPERTIE = ["水", "土"]

    # BUFF
    ATTACK = 2
    DEFENSE = 1
    VITALITY = -1


class Wood(Propertie):
    NAME = "木"
    RESTRAINED_PROPERTIE = "土"
    DISSOLVE_PROPERTIE = ["水", "火"]

    # BUFF
    ATTACK = -1
    DEFENSE = 1
    VITALITY = 2


class Water(Propertie):
    NAME = "水"
    RESTRAINED_PROPERTIE = "火"
    DISSOLVE_PROPERTIE = ["金", "木"]

    # BUFF
    ATTACK = -1
    DEFENSE = 2
    VITALITY = 1


class Fire(Propertie):
    NAME = "火"
    RESTRAINED_PROPERTIE = "金"
    DISSOLVE_PROPERTIE = ["火", "土"]

    # BUFF
    ATTACK = 4
    DEFENSE = -1
    VITALITY = -1


class Earth(Propertie):
    NAME = "土"
    RESTRAINED_PROPERTIE = "水"
    DISSOLVE_PROPERTIE = ["火", "金"]

    # BUFF
    ATTACK = -1
    DEFENSE = 4
    VITALITY = -1