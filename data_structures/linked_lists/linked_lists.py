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


