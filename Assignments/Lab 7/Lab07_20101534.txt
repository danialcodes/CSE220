# Task 1 on Key index Searching & Sorting
'''If the question doesn't limit me to use only 2 instence variable
i'll use max and min as self.max and self.min to reduce code repetation
in search() and sort() method
'''

class KeyIndex:
#     k = [0]
    def __init__(self,a):
        self.k = [0]
        self.passed_array = a
        _min = min(a)
        _max = max(a)
        if(_min>0):
            _min = 0

        self.k*= ( _max+1 + _min*-1)
        
        for i in a:
            self.k[ i+(_min*-1)]+=1
            
    def __str__(self):
        return str(self.passed_array)
    
    def search(self,val):
        _max , _min = max(self.passed_array) , min(self.passed_array)
        if(_min>0):
            _min = 0
            
        if(val<=_max and val>=_min and self.k[val+(_min*-1)]):
            return True
        return False
    
    def sort(self):
        indx = 0
        _min = min(self.passed_array)
        if(_min>0):
            _min = 0
        for i in range(len(self.k)):
            for j in range(self.k[i],0,-1):
                self.passed_array[indx]=i-(_min*-1)
                indx+=1
        return self.passed_array
        


print("\n//=======Task 1 -- Key index Searching & Sorting=======//")

print("\n//For Positive and distinct integers //")
arr1 = [5,1,4,10,7,9,15]
KI1 = KeyIndex(arr1)
print("Initial Array:",KI1)
print("Searching 7 ...")
print("Result:",KI1.search(7))
print("Searching 20 ...")
print("Result:",KI1.search(20))
print("Sorted Array:",KI1.sort())

print("\n//For Negetive/Positive and distinct,non-distinct integers //")
arr2 = [-14,-20,-5,-10,0,5,16]
KI2 = KeyIndex(arr2)
print("Initial Array:",KI2)
print("Searching -14 ...")
print("Result:",KI2.search(-14))
print("Searching 16 ...")
print("Result:",KI2.search(16))
print("Sorted Array:",KI2.sort())




# Task 2 on Hashing
class HashTable:
    def __init__(self,a):
        self.k = [0]*9
        for i in a:
            h = self.cal_hash(i)
            if(self.k[h]):
                while(self.k[h]):
                    h=(h+1)%9
                self.k[h]=i
            else:
                self.k[h]=i
            
    @staticmethod
    def cal_hash(val):
        v = "AEIOU"
        c_count = 0
        v_sum = 0
        for i in val:
            if(i>="0" and i<="9"):
                v_sum+=int(i)
            elif( i not in v):
                c_count+=1
        return (c_count*24+v_sum)%9
#     Just made search method for trying, it's not perfect if collition present
    def search(self,val):
        h = self.cal_hash(val)
        if(self.k[h]==val):
            return True
        return False




print("\n//=======Task 2 -- Hashing=======//")
arr2 = ["ST1E89B8A32","KDFD24SDDC4D","DSUI5D4DVDDD","74SD74DVVDV","43VDV4V35SD","SDSDVDV354DDV4","BKSDDSVJN55SDV","52DDSVSD","KHNSDVDS54DVC7"]
ht1 = HashTable(arr2)
print("\nPrevious array:",arr2)
print("\nHashtable:",ht1.k)

