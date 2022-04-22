# Task 1
def findMax(arr,maxim,max_indx,i):
    if(i==0):
        return maxim,max_indx
    
    if(arr[i]>maxim):
            maxim = arr[i]
            max_indx = i
            
    return findMax(arr,maxim,max_indx,i-1)
    
def recur_selection_sort(arr,i):
    if(i==0):
        return arr
    maxim,max_indx = findMax(arr,arr[0],0,i) 
    temp = arr[i]
    arr[i]=maxim
    arr[max_indx]=temp
    return recur_selection_sort(arr,i-1)
    
print("\n//=======Task 1 -- Array Recursively Sorting with selection sort=======//")

arr1= [60,50,40,30,20,10,70]
print("Before Sorting: ",arr1)
print("After Sorting: ",recur_selection_sort(arr1,len(arr1)-1))





# Task 2
def insertIfPossible(arr,i):
    if(i==-1):
        return
    if (arr[i]>arr[i+1]):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        return insertIfPossible(arr,i-1)
    return 

def recur_insertion_sort(arr,i=0):
    if(i==len(arr)):
        return arr
    insertIfPossible(arr,i-1) 
    return recur_insertion_sort(arr,i+1)
print("\n//=======Task 2 -- Array Recursively Sorting with Insertion Sort=======//")

arr2 = [100,90,80,70,60,65,69,50]
print("Before Sorting: ",arr2)
print("After Sorting: ",recur_insertion_sort(arr2))




# Task 3-4
class singleNode:
    def __init__(self,v=None,n=None):
        self.value = v
        self.next = n
class singlyLinkedList:
    size = 0
    def __init__(self,iterable):
        self.head = None
        tail = None
        for i in iterable:
            self.size+=1
            node = singleNode(i,None)
            if(self.head is None):
                self.head = node
                tail = self.head
            else:
                tail.next = node
                tail = node
    def __str__(self):
        node = self.head
        r = ""
        while(node is not None):
            r+=str(node.value)+" "
            node = node.next
        return r
    # Task 3
    def bubbleSort(self):
        for i in range(self.size-1,-1,-1):
            itr = self.head
            for j in range(i):
                if(itr.value>itr.next.value):
                    temp = itr.next.value
                    itr.next.value = itr.value
                    itr.value = temp
                itr= itr.next
    # Task 4
    def selectionSort(self):
        for i in range(self.size-1,-1,-1):
            itr = self.head
            maxim = itr.value
            max_node = self.head
            for j in range(i+1):
                if(itr.value>maxim):
                    maxim = itr.value
                    max_node = itr
                if(j!=i):
                    itr = itr.next
            temp = itr.value
            itr.value=maxim
            max_node.value=temp




print("\n//=======Task 3 -- Singly Linked List Sorting with Bubble Sort=======//")
arr3 = [60,70,50,40,30,20,10,80]
ll1 = singlyLinkedList(arr3)
print("Before Sorting: ",ll1)
ll1.bubbleSort()
print("After Sorting: ",ll1)

print("\n//=======Task 4 -- Singly Linked List Sorting with Selection Sort=======//")
arr4 = [50,60,70,10,20,30,5,2]
ll2 = singlyLinkedList(arr4)
print("Before Sorting: ",ll2)
ll2.selectionSort()
print("After Sorting: ",ll2)




# Task 5
class doubleNode:
    def __init__(self,v=None,p=None,n=None):
        self.value = v
        self.next = n
        self.prev = p

class DoublyLinkedList:
    size = 0
    def __init__(self,arr):
        self.head = doubleNode(None, None, None)
        self.head.next = self.head.prev = self.head

        self.head.next = None
        tail = None
        for item in arr:
            self.size+=1
            newNode = doubleNode(item, None, None)
            if self.head.next == None:
                self.head.next = newNode
                self.head.prev = newNode
                newNode.prev = self.head
                newNode.next = self.head

                tail = newNode

            else:
                newNode.next = self.head
                newNode.prev = tail
                tail.next = newNode
                self.head.prev = newNode

                tail = newNode
    def __str__(self):
        itr = self.head.next
        r = ""
        while(itr is not self.head):
            r+=str(itr.value)+"  "
            itr = itr.next
        return r
#     Task 5
    def insertionSort(self):
        itr = self.head.next
        while(itr!=self.head):
            
            itr2= itr.prev
            while(itr2!=self.head):
                
                if (itr2.value>itr2.next.value):
                    temp = itr2.value
                    itr2.value = itr2.next.value
                    itr2.next.value = temp
                    itr2 = itr2.prev
                else:
                    break
            itr = itr.next
            





print("\n//=======Task 5 -- Doubly Linked List Sorting with Insertion Sort=======//")

arr5 = [50,20,10,30,40]
dl1 = DoublyLinkedList(arr5)
print("Before Sorting: ",dl1)

dl1.insertionSort()
print("After Sorting: ",dl1)




# Task 6

def recur_binarySearch(arr,num,r,l=0):
    if(l>r):
        return -1
    m = (l+r)//2
    if(arr[m]==num):return m
    elif(arr[m]>num):
        r=m-1
    else:
        l=m+1
    return recur_binarySearch(arr,num,r,l)

print("\n//=======Task 6 -- Array item Recursively Searching with Binary Search=======//")

bs = [10,20,30,40,50,60,70]
print("Main array:",bs)
findable = 7
print("Find ",findable)
print("Index: ",recur_binarySearch(bs,findable,len(bs)-1))
print("Main array:",bs)

findable = 40
print("Find ",findable)
print("Index: ",recur_binarySearch(bs,findable,len(bs)-1))




# Task 7
global_arr = [0]*9999
def recursive_memoiz_fibo(n):
    if(n<0):
        return "Fibonacci Number starts from 0"
    if(n==0):
        return 0
    if(global_arr[n]>0):
        return global_arr[n]
    if(n==1 or n==2):
        global_arr[n] = 1
    else:
        global_arr[n] = recursive_memoiz_fibo(n-1)+recursive_memoiz_fibo(n-2)
    return global_arr[n]


print("\n//=======Task 7 -- nth Fibonacci Number with recursive memoization=======//")
print("5th fibonacci is",end=" ")
print(recursive_memoiz_fibo(5))






