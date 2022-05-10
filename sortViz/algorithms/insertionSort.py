import time
# Importing colors from colors.py
from utils.colors import *
import msvcrt as m


def insertion_sort(data, drawData, timeTick):

    for i in range(1, len(data)):
        key = data[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        drawData(data, [YELLOW if x == j + 1 else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])

