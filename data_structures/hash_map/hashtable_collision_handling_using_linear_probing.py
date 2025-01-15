class Hashtable:
    def __init__(self):
        self.max=10
        self.arr=[None for i in range(self.max)]
    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash%self.max
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]
    def __getitem(self,key):
        h=self.get_hash(key)
        for prob_index in range(self.get_prob_range(h)):
            element=self.arr[prob_index]
            if element is None:
                return
            if element[0]==key:
                return element[1]