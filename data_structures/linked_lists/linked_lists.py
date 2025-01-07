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

    def insert_at(self,data,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_begining(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
    def remove_at(self,data,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1


if __name__=='__main__':
    l1=Linkedlist()
    l1.insert_at_begining(10)
    l1.insert_at_end(20)
    l1.insert_at(10,2)
    # l1.insert_values(["banana","mango","grapes","orange"])
    l1.print()
    l1.get_length()



