class MyHashMap:

    def __init__(self):
        self.keys = [False] * 1000001
        self.values = [-1] * 1000001
        

    def put(self, key: int, value: int) -> None:
        self.keys[key] = True
        self.values[key] = value
        

    def get(self, key: int) -> int:
        if self.keys[key] == True:
            return self.values[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if self.keys[key] == True:
            self.keys[key] = False
            self.values[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)