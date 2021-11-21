class Node:
    def __init__(self, e, n):
        self.elem = e
        self.next = n

class LinkedList:

    def __init__(self, a):
        self.head = None #instance variable
        #write your code here

    def showList(self):
        #write your code here
        pass

    def isEmpty(self):
        #write your code here
        return True

    def clear(self):
        #write your code here
        pass

    def insert(self, newElement, index = None):
        #write your code here
        pass

    def remove(self, deleteKey):
        #write your code here
        return None

    def evenList(self):
        #write your code here
        return None

    def find(self, element):
        #write your code here
        return False

    def reverseList(self):
        #write your code here
        pass

    def sort(self):
        #write your code here
        pass

    def sum(self):
        #write your code here
        return -1

    def rotateKTimes(self, k, direction):
        #write your code here
        pass

#==========================Tester Code==========================#
        
#Task-2.1, 2.2 -- Constructor & showList
print("\n//=======Task 2.1, 2.2 -- Constructor & showList=======//")
a = [10, 20, 30, 40, 50, 60]
l1 = LinkedList(a)
l1.showList() #Should print: 10->20->30->40->50->60

#Task-2.3 -- isEmpty
print("\n//========Task 2.3 -- isEmpty========//")
isListEmpty = l1.isEmpty()
print(isListEmpty) #Should print: false
b = []
l2 = LinkedList(b)
isListEmpty = l2.isEmpty()
print(isListEmpty) #Should print: true

#Task-2.4 -- Clear
print("\n//=======Task 2.4 -- Clear =======//")
print("Before clearing Linked List")
l1.showList() #Should print: 10->20->30->40->50->60
l1.clear()
print("After clearing Linked List")
l1.showList() #Should print: Empty List

#Task-2.5, 2.6 -- Insert
print("\n//=======Task 2.5, 2.6 -- Insert=======//")
c = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3 = LinkedList(c)
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

#Task-2.8 -- EvenList
print("\n//=======Task 2.8 -- EvenList =======//")
d = [1, 2, 5, 3, 8]
l4 = LinkedList(d)
l5 = l4.evenList()
l5.showList() #Should print: 2->8

#Task-2.9 -- Find
print("\n//=======Task 2.9 -- Find =======//")
found = l4.find(5)
print(found) #Should print: true
found = l4.find(4)
print(found) #Should print: false

#Task-2.10 -- Reverse List
print("\n//=======Task 2.10 -- Reverse =======//")
print("Before Reverse: ", end='')
l4.showList() #Should print: 1->2->5->3->8
l4.reverseList()
print("After Reverse: ", end='')
l4.showList() #Should print: 8->3->5->2->1

#Task-2.11 -- Sort
print("\n//=======Task 2.11 -- Sort =======//")
print("Before Sort: ", end='')
l4.showList() #Should print: 8->3->5->2->1
l4.sort()
print("After Sort: ", end='')
l4.showList() #Should print: 1->2->3->5->8

#Task-2.12 -- Sum of Elements
print("\n//=======Task 2.12 -- Sum of Elements =======//")
l4.showList() #Should print: 1->2->3->5->8
total = l4.sum()
print("Sum of Elements:", total)

#Task-2.13 -- Rotate
print("\n//=======Task 2.13 -- Rotate =======//")
l4.showList() #Should print: 1->2->3->5->8
l4.rotateKTimes(2, "left")
l4.showList() #Should print: 3->5->8->1->2
l4.rotateKTimes(2, "right")
l4.showList() #Should print: 1->2->3->5->8