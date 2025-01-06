class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head=None
    #Method to print linked list
    def print(self):
        if self.head==None:
            print("Linked list is empty")
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->' if itr.next else str(itr.data)
            itr=itr.next
        print(llstr)
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def get_length(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    



if __name__=='__main__':
    l1=Linkedlist()
    l1.insert_at_begining(10)
    l1.insert_at_end(20)
    l1.insert_values(["banana","mango","grapes","orange"])
    l1.print()
    l1.get_length()



