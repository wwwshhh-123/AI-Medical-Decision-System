def assess(damage, temperature):
    """
    风险分级系统（比赛关键点）
    """

    if damage > 60 or temperature > 200:
        return "DANGER"
    elif damage > 25 or temperature > 120:
        return "WARNING"
    else:
        return "SAFE"