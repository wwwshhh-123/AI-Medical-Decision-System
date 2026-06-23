import numpy as np

def simulate(power, duration):
    """
    组织物理模拟：温度 + 损伤
    """

    # 温度模型（核心比赛亮点）
    temperature = 37 + (power * 0.8) + (duration * 1.2)

    # 损伤模型（指数增长）
    damage = (power * duration) * 0.06

    # 限制范围（防炸图）
    temperature = min(300, temperature)
    damage = min(100, damage)

    return float(temperature), float(damage)