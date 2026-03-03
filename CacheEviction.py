from collections import deque


def load_data(file_path):
    with open(file_path, 'r') as file:
        x = file.readline()
        print(x)
class FIFO:
    def __init__(self, capacity):
        self.capacity = capacity
        self.misses = 0


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.misses = 0

class OPTFF:
    def __init__(self, capacity):
        self.capacity = capacity
        self.misses = 0




    
print(load_data("data.txt"))

