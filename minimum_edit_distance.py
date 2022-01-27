import numpy as np
def min_distance(s, t):
    source = [i for i in s]
    target = [i for i in t]
    array = np.zeros((len(source), len(target)))

    array[0] = [j for j in range(len(target))]
    array[:, 0] = [j for j in range(len(source))]
    for i in range(1, len(target)):
        for r in range(1, len(source)):
            if source[r] != target[i]:
                array[r, i] = min(array[r - 1, i], array[r, i - 1]) + 1
            else:
                array[r, i] = array[r - 1, i - 1]
    return int(array[len(source) - 1, len(target) - 1])

