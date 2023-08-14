import numpy as np

def gera_valor(media):
    random_float = np.random.normal(media, 1.0)

    # Round the floating-point number to the nearest integer
    random_integer = max(int(round(random_float)), 1)

    return random_integer
