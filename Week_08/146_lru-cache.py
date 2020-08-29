from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        # 限定大小的字典
        self.maxsize = capacity
        self.lrucache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
            return self.lrucache.get(key)
        else:
            return -1

    def put(self, key: int, value: int):
        if key in self.lrucache:
            del self.lrucache[key]
        self.lrucache[key] = value
        if len(self.lrucache) > self.maxsize:
            #false = FIFO true=FILO
            self.lrucache.popitem(last=False)

