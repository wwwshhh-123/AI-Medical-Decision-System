import numpy as np
import pandas as pd

def generate_data(n=300):

    data = []

    for _ in range(n):

        lesion_size = np.random.uniform(1, 10)
        depth = np.random.uniform(1, 10)

        power = lesion_size * 10 + np.random.normal(0, 1)
        duration = depth * 1.5 + np.random.normal(0, 0.2)

        damage = power * duration * 0.05 + np.random.normal(0, 0.5)

        data.append([lesion_size, depth, power, duration, damage])

    df = pd.DataFrame(data, columns=[
        "lesion_size", "depth", "power", "duration", "damage"
    ])

    return df


if __name__ == "__main__":
    df = generate_data()
    print(df.head())