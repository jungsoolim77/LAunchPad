import time
# Importing colors from colors.py
from utils.colors import *
import msvcrt as m


def selection_sort(data, drawData, timeTick):

    for i in range(len(data)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        # Swap the found minimum element with
        # the first element
        data[i], data[min_idx] = data[min_idx], data[i]

        drawData(data, [YELLOW if x == i else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
