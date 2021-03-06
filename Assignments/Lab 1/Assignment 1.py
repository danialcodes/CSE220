#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Linear Array
# 1
def shiftLeft(source, k):
    for i in range(len(source)):
        if (i >= len(source) - 3):
            source[i] = 0
        else:
            source[i] = source[i + k]


source = [10, 20, 30, 40, 50, 60]
shiftLeft(source, 3)
print(source)


# In[11]:


# Linear Array
# 2
def rotateLeft(source, k):
    new_arr = [0] * len(source)
    src_index = k
    for i in range(len(source)):
        new_arr[i] = source[src_index]
        src_index = (src_index + 1) % (len(source))
    return new_arr


source = [10, 20, 30, 40, 50, 60]
rotated_array = rotateLeft(source, 3)
print(rotated_array)


# In[7]:


# Linear Array
# 3
def remove(source, size, idx):
    for i in range(idx + 1, size):
        source[i - 1] = source[i]
    source[size - 1] = 0


source = [10, 20, 30, 40, 50, 0, 0]
remove(source, 5, 2)
print(source)


# In[16]:


# Linear Array
# 4
def removeAll(source, size, element):
    new_arr = [0] * len(source)
    nw_index = 0
    for i in range(size):
        if source[i] != 2:
            new_arr[nw_index] = source[i]
            nw_index += 1
    return new_arr


source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
source = removeAll(source, 7, 2)
print(source)


# In[21]:


# Linear Array
# 5
def check_balance(source):
    first = 0
    last = 0
    check = 'false'
    for i in range(len(source)):
        j = len(source) - i
        for fst in range(i):
            first += source[fst]
        for lst in range(i, len(source)):
            last += source[lst]
        if (first == last):
            check = 'true'
            break
        first = 0
        last = 0
    print(check)


source = [10, 3, 1, 2, 10]
check_balance(source)


# In[54]:


# Linear Array
# 6
def make_array(n):
    array = [0] * n * n
    indx = n * n - 1
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            array[indx] = j
            indx -= 1
        #             print("i =",i,"j =",j)
        indx -= (n - i)
    return array


array = make_array(4)
print(array)


# In[79]:


# Linear Array
# 7
def count_max_bunch(array):
    c_max = 0
    temp_max = 0
    for i in range(len(array)):
        if (i == 0):
            previous = array[i]
            c_max = 1
        elif (array[i] == previous):
            c_max += 1
        else:
            if (c_max > temp_max):
                temp_max = c_max
            c_max = 1
            previous = array[i]
    if (temp_max > c_max):
        return temp_max
    return c_max


array = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 4, 4, 4]
print(count_max_bunch(array))


# In[126]:


# Linear Array
# 8
def check_repetition(array):
    new_array = [0] * len(array) * 2
    nw_indx = 0
    size = 0
    for i in range(len(array)):
        is_present = False

        j = 0
        while (j < len(new_array)):
            if (new_array[j] == array[i]):
                is_present = True
                indx = j
                j = len(new_array)
            j += 2

        if (is_present):
            new_array[indx + 1] += 1

        else:
            new_array[nw_indx] = array[i]
            new_array[nw_indx + 1] = 1
            nw_indx += 2
            size += 1
    r = [0] * size
    a = 0
    for i in range(1, size * 2, 2):
        if (new_array[i] > 1):
            r[a] = new_array[i]
            a += 1
    for i in range(a):
        for j in range(i + 1, a):
            if (r[i] == r[j]):
                return True
    return False


array = [4, 5, 6, 6, 4, 3, 6, 4]
print(check_repetition(array))


# In[136]:


# Circular Array
# 1
def check_palindrome(cir, size, start):
    lst_index = (start + size - 1) % len(cir)
    isPalindrome = True
    for i in range(size):
        if (cir[start] != cir[lst_index]):
            isPalindrome = False
            return isPalindrome
        start = (start + 1) % (len(cir))
        lst_index -= 1
        if (lst_index < 0):
            lst_index = len(cir) - 1
    return isPalindrome


source = [10, 20, 0, 0, 0, 10, 20, 30]
print(check_palindrome(source, 5, 5))


# In[149]:


# Circular Array
# 2
def return_linear(cir1, start_1, size_1, cir2, start_2, size_2):
    temp_start_2 = start_2
    matched = [0] * size_1
    match_count = 0
    for i in range(size_1):
        for j in range(size_2):
            if (cir1[start_1] == cir2[start_2]):
                matched[match_count] = cir1[start_1]
                match_count += 1
            start_2 = (start_2 + 1) % len(cir2)
        start_1 = (start_1 + 1) % len(cir1)
        start_2 = temp_start_2
    nw_arr = [0] * match_count
    for i in range(match_count):
        nw_arr[i] = matched[i]
    return nw_arr


cir1 = [40, 50, 0, 0, 0, 10, 20, 30]
cir2 = [10, 20, 5, 0, 0, 0, 0, 0, 5, 40, 15, 25]
common_linear = return_linear(cir1, 5, 5, cir2, 8, 7)
print(common_linear)

# In[211]:


# Circular Array
# 3
import random


def play_musical_chair(players):
    start = 0
    size = 7
    remaning_players = [0] * size

    while (size > 1):
        #         print("start",players)
        temp = players[size - 1]
        for i in range(size - 1, 0, -1):
            players[i] = players[i - 1]
        players[0] = temp
        #         print("changed",players)
        if (random.randint(0, 3) == 1):
            indx = size // 2
            #             print("Removing",players[indx])

            for i in range(indx, size - 1):
                players[i] = players[i + 1]
            players[size - 1] = 0
            #             print("Removed",players)
            size -= 1
            if (size == 1):
                print("Winner is", players[0], "!!!!")
            else:
                for i in range(size):
                    print(players[i], end=" ")
                print()

        start += 1


#         print("last",players)


players = ['Danial', 'Nishat', 'Shohardo', 'Robin', 'Luffy', 'Naruto', 'Kilua']
play_musical_chair(players)



