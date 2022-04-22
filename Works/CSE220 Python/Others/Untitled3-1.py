#!/usr/bin/env python

# coding: utf-8

# In[90]:


#Task01

class Node:

    def __init__(self,value,next):
        self.value = value
        self.next = next

#Task02

class MyList:

    def __init__(self, a):
        self.head = None
        for i in range(len(a)):
            new = Node(a[i],None)
            if(self.head == None):
                self.head = new
                tail = new
            else:
                tail.next = new
                tail = new
                
    def showList(self):
        n = self.head
        count = 0
        while (n != None):
            count += 1
            n = n.next

        if (count == 0):
            print("Empty List")
        else:
            n = self.head
            while (n != None):
                print(n.value,end=' ')
                n = n.next
        print()

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def clear(self):
        node = self.head
        if node.value == None:
            return
        while node != None:
            node.value = None
            node = node.next
        self.head = None

    def size(self):
        return self.size

    def insert(self, val,index=None):
        if(self.element_Find(val)):
            print("key already exists!")
            return
        if (index==None):
            n = Node(val, None)
            if self.head is None:
                self.head = n
            else:
                i = self.head
                while(i.next is not None):
                    i = i.next
                i.next = n
        else:
            n = self.head
            count = 0
            while (n != None):
                count += 1
                n = n.next
            if (index < 0 or index > count):
                raise IndexError
            n = Node(val, None)

            if index == 0:
                n.next = self.head
                self.head = n
            else:
                pred = self.nodeAt(index - 1)
                n.next = pred.next
                pred.next = n

    def nodeAt(self, index):
        count = 0
        n = self.head
        while (n != None):
            count += 1
            n = n.next
        if (index < 0 or index > count):
            return None
        n = self.head
        for i in range(index):
            n = n.next
        return n

        

    def remove(self, deleteKey):
        node = self.head
        if node.value == None:
            return'key Not found'
        while node is not None:
            if(node.value == deleteKey):
                node.value = node.next.value
                node.next = node.next.next
                return deleteKey
            if(node.next.value == deleteKey):
                node.next = node.next.next
                return deleteKey
            node = node.next
        return'key Not found'

        
#Task 3

    def even(self):
        n = self.head
        l = None
        while n is not None:
            if n.value % 2 == 0:
                if(l == None):
                    l = MyList([n.value])
                else:
                    l.insert(n.value)
            n = n.next
        return l

    def element_Find(self,key):
        n=self.head
        while n is not None:
            if n.value==key:
                return True
    
            n=n.next
        return False
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 
        
    def listSort(self):
        n=self.head
        i=n
        while i is not None:
            j=i.next
            while j is not None:
                if i.value>j.value:
                    i.value,j.value=j.value,i.value
                j=j.next
            i=i.next
            
    def listSum(self):
        n=self.head
        s=0
        while n is not None:
            s+=n.value
            n=n.next
        return s
    def rotate(self,d,t):
        count = 0
        n = self.head
        while (n != None):
            count += 1
            n = n.next
        if(d=="left"):
            for i in range(t):
                LastNode = self.nodeAt(count-1)
                Head = self.head.next
                self.head.next = None
                LastNode.next = self.head
                self.head = Head
        elif(d=="right"):
            for i in range(t):
                LastNode = self.nodeAt(count-2)
                Head = LastNode.next
                LastNode.next = None
                Head.next = self.head
                self.head = Head


# In[ ]:





# In[102]:


a = [10, 20, 30, 40, 50, 60]
l1 = MyList(a)
l1.showList()
isListEmpty = l1.isEmpty()
print(isListEmpty)
b = []
l2 = MyList(b)
isListEmpty = l2.isEmpty()
print(isListEmpty)
print("Before clearing Linked List")
l1.showList()
l1.clear()
print("After clearing Linked List")
l1.showList()
c = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3 = MyList(c)
l3.showList()
l3.insert(100)
l3.showList()
l3.remove(100)
l3.showList()
d = [1, 2, 5, 3, 8]
l4 = MyList(d)
l5 = l4.even()
l5.showList()
found = l4.element_Find(5)
print(found)
found = l4.element_Find(4)
print(found)

print("Before Reverse: ", end='')
l4.showList() 
l4.reverse()
print("After Reverse: ", end='')
l4.showList() 

print("Before Sort: ", end='')
l4.showList()
l4.listSort()
print("After Sort: ", end='')
l4.showList()
l4.showList()
total = l4.listSum()
print("Sum of Elements:", total)
l4.showList() 
l4.rotate("left",2)
l4.showList()
l4.rotate("right",2)
l4.showList()


# In[ ]:




