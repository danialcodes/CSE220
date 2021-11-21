#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task 1
class Node:
    def __init__(self,d,n):
        self.data = d
        self.next = n


# In[2]:


class MyList:
#   Task 2.1.a
    def __init__(self,iterable):
        self.head = None
        tail = None
        for i in iterable:
            presentNode = Node(i,None)
            if(self.head is None):
                self.head = presentNode
                tail = self.head
            else:
                tail.next = presentNode
                tail = presentNode
#   Task 2.2
    def showList(self):
        if (self.head is None):
            print("Empty list")
        else:
            itr = self.head
            while (itr is not None):
                if(itr.next is None):
                    print(itr.data)
                else:
                    print(itr.data,end=" -> ")
                itr = itr.next
#   Task 2.3
    def isEmpty(self):
        if(self.head is None):
            return True
        return False
#   Task 2.4
    def clear(self):
        if(not self.isEmpty()):
            self.head = None
#   Self made method to reduce code rewritting
    def findIndex(self,element):
        itr = self.head
        count = 0
        while (itr is not None):
            if (itr.data == element):
                return count
            itr = itr.next
            count+=1
        return False
#   Self made method to reduce code rewritting
    def size(self):
        itr = self.head
        count = 0
        while(itr is not None):
            count+=1
            itr = itr.next
        return count
#   Self made method to reduce code rewritting
    def nodeAt(self,index):
        if(index>=0 and index<self.size()):
            itr = self.head
            count = 0
            while(count<index):
                itr = itr.next
                count+=1
            return itr
#   Task 2.5 - 2.6
    def insert(self, newElement,index=None):
        if(index == None):
            if (self.findIndex(newElement)):
                print("key {} already exists!".format(newElement))
                return
            tail = Node(newElement,None)
            lastNode = self.nodeAt(self.size()-1)
            lastNode.next = tail
        else:
            if (not self.isEmpty()):
                size = self.size()
                if (index>=0 and index<=size):
                    if (self.findIndex(newElement)):
                        print("key {} already exists!".format(newElement))
                        return
                    if(index==0):
                        newNode = Node(newElement,self.head)
                        self.head = newNode
                    elif(index==size):
                        preNode = self.nodeAt(index-1)
                        newNode = Node(newElement,None)
                        preNode.next = newNode
                    else:  
                        preNode = self.nodeAt(index-1)
                        newNode = Node(newElement,preNode.next)
                        preNode.next = newNode
#   Task 2.7
    def remove(self, deletekey):
        if (not self.isEmpty()):
            if(self.head.data == deletekey):
                self.head = self.head.next
            else:
                delIndex = self.findIndex(deletekey)
                if(delIndex):
                    preDelItem = self.nodeAt(delIndex-1)
                    preDelItem.next = preDelItem.next.next
                    return deletekey
                else:
                    print("Key {} does not exist".format(deletekey))
#    Task 3.1
    def makeEvenList(self):
        itr = self.head
        count = 0
        evenList = None
        while (itr is not None):
            if(itr.data%2==0):
                if(count == 0):
                    evenList = MyList([itr.data])
                else:
                    evenList.insert(itr.data)
                count+=1
            itr = itr.next
        return evenList
#     Task 3.2
    def find(self,element):
        if (self.findIndex(element)):
            return True
        return False
#     Task 3.3
    def reverse(self):
        itr = self.head
        newHead = None
        while (itr is not None):
            nextElement = itr.next
            itr.next = newHead
            newHead = itr
            itr = nextElement
        self.head = newHead
#     Task 3.4
    def sort(self):
        itr = self.head
        while (itr is not None):
            next = itr.next
            while (next is not None):
                if(itr.data>next.data):
                    temp = next.data
                    next.data = itr.data
                    itr.data = temp
                next = next.next
            itr = itr.next
                
#     Task 3.5
    def total(self):
        count = 0
        itr = self.head
        while (itr is not None):
            count+=itr.data
            itr = itr.next
        return count
#   Self made method to reduce code writting
    def rotateLeft(self):
        newHead = self.head.next
        preLastNode = self.nodeAt(self.size()-1)
        self.head.next = None
        preLastNode.next = self.head
        self.head = newHead
#   Self made method to reduce code writting
    def rotateRight(self):
        newLastNode = self.nodeAt(self.size()-2)
        newHead = newLastNode.next
        newLastNode.next = None
        newHead.next = self.head
        self.head = newHead
#     Task 3.6
    def rotateKTimes(self,d,t):
        if(d.lower()=='left'):
            count = 0
            while (count<t):
                self.rotateLeft()
                count+=1
        elif(d.lower()=='right'):
            count = 0
            while (count<t):
                self.rotateRight()
                count+=1


# In[3]:


#==========================Tester Code==========================#


# In[4]:


#Task-2.1, 2.2 -- Constructor & showList
print("\n//=======Task 2.1, 2.2 -- Constructor & showList=======//")
a = [10, 20, 30, 40, 50, 60]
l1 = MyList(a)
l1.showList() #Should print: 10->20->30->40->50->60


# In[5]:


#Task-2.3 -- isEmpty
print("\n//========Task 2.3 -- isEmpty========//")
isListEmpty = l1.isEmpty()
print(isListEmpty) #Should print: false
b = []
l2 = MyList(b)
isListEmpty = l2.isEmpty()
print(isListEmpty) #Should print: true


# In[6]:


#Task-2.4 -- Clear
print("\n//=======Task 2.4 -- Clear =======//")
print("Before clearing Linked List")
l1.showList() #Should print: 10->20->30->40->50->60
l1.clear()
print("After clearing Linked List")
l1.showList() #Should print: Empty List


# In[7]:


#Task-2.5, 2.6 -- Insert
print("\n//=======Task 2.5, 2.6 -- Insert=======//")
c = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3 = MyList(c)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90
l3.insert(100)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100
l3.insert(0, 0)
l3.showList() #Should print: 0->10->20->30->40->50->60->70->80->90->100
l3.insert(110, 5)
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100
l3.insert(120, 12)
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
l3.insert(50) #Should print: Key 50 already exists


# In[8]:


#Task-2.7 -- Remove
print("\n//=======Task 2.7 -- Remove=======//")
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(0)
l3.showList() #Should print: 10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(110) 
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100->120
l3.remove(120)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100
l3.remove(120) #Should print: Key 120 does not exist


# In[9]:


#Task-2.8 -- EvenList
print("\n//=======Task 2.8 -- EvenList =======//")
d = [1, 2, 5, 3, 8]
l4 = MyList(d)
l5 = l4.makeEvenList()
l5.showList() #Should print: 2->8


# In[10]:


#Task-2.9 -- Find
print("\n//=======Task 2.9 -- Find =======//")
found = l4.find(5)
print(found) #Should print: true
found = l4.find(4)
print(found) #Should print: false


# In[11]:


#Task-2.10 -- Reverse List
print("\n//=======Task 2.10 -- Reverse =======//")
print("Before Reverse: ", end='')
l4.showList() #Should print: 1->2->5->3->8
l4.reverse()
print("After Reverse: ", end='')
l4.showList() #Should print: 8->3->5->2->1


# In[12]:


#Task-2.11 -- Sort
print("\n//=======Task 2.11 -- Sort =======//")
print("Before Sort: ", end='')
l4.showList() #Should print: 8->3->5->2->1
l4.sort()
print("After Sort: ", end='')
l4.showList() #Should print: 1->2->3->5->8


# In[13]:


#Task-2.12 -- Sum of Elements
print("\n//=======Task 2.12 -- Sum of Elements =======//")
l4.showList() #Should print: 1->2->3->5->8
total = l4.total()
print("Sum of Elements:", total)


# In[14]:


#Task-2.13 -- Rotate
print("\n//=======Task 2.13 -- Rotate =======//")
l4.showList() #Should print: 1->2->3->5->8
l4.rotateKTimes("left",2)
l4.showList() #Should print: 3->5->8->1->2
l4.rotateKTimes("right",2)
l4.showList() #Should print: 1->2->3->5->8

