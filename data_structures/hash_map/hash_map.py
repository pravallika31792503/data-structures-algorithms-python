class HashTable:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]
    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        print( hash%self.max)
    def __getitem__(self,index):
        h=self.get_hash(index)
        return self.arr[h]
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val

t=HashTable()
t.get_hash("march 7")
# t["march 7"]=120
