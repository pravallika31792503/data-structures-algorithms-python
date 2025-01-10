class HashTable:
    def __init__(self):
        self.max=100
        self.arr=[[] for i in range(self.max)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.max
    def __getitem__(self,key):
        h=self.get_hash(key)
        for i in self.arr[h]:
            if i[0]==key:
                return i[1]
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found=False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,value)
                found=True
        if not found :
            self.arr[h].append((key,value))
    def __delitem__(self,key):
        h=self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                print('index',idx)
                del self.arr[h][idx]

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
t['march 6']
 