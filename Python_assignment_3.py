#Q-1 Python Program for Find reminder of array multiplication divided by n
def findremainder(arr, lens, n):
   mul = 1
   # find the individual remainder
   for i in range(lens):
      mul = (mul * (arr[i] % n)) % n
   return mul % n
# Driven code
arr = [100,1,2,3,4,5,6,6,7]
lens = len(arr)
n = 11
print( findremainder(arr, lens, n))

#Q-2 Python Program to check if given array is Monotonic
def isMonotonic(A):
   return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
      all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
# main
A = [1,2,3,4,7,8]
print(isMonotonic(A))

#Q-3 Python program to interchange first and last elements in a list
#swap first and last element in list

# Swap function
def swapList(sl):
    n = len(sl)
      
    # Swapping 
    temp = sl[0]
    sl[0] = sl[n - 1]
    sl[n - 1] = temp
      
    return sl
      
l = [10, 14, 5, 9, 56, 12]

print(l)
print("Swapped list: ",swapList(l))

#Q-4 Python program to swap two elements in a list

# Python program to swap two elements in a list

# user-defined function
def swap(l, p1, p2):
   l[p1], l[p2] = l[p2], l[p1]
   return l

# take inputs
l = [1, 2, 3, 4, 5]

# print list
print("List:", l)

# print new list
p1, p2 = 1, 2
print("New List:", swap(l, p1-1, p2-1))

#Q-5 write a program to find length of list

# Python code to demonstrate
# length of list
# using naive method
 
# Initializing list
test_list = [ 1, 4, 5, 7, 8 ]
 
# Printing test_list
print ("The list is : " + str(test_list))
 
# Finding length of list
# using loop
# Initializing counter
counter = 0
for i in test_list:
     
    # incrementing counter
    counter = counter + 1
 
# Printing length of list
print ("Length of list using naive method is : " + str(counter))

#Q-6 write a program to check if element exists in list
listA = [[-9, -1, 3], [11, -8],[-4,434,0]]
search_element = -8

# Given list
print("Given List :\n", listA)

print("Element to Search: ",search_element)

# Using in
if any(search_element in sublist for sublist in listA):
   print("Present")
else:
   print("Not Present")

#Q-7 write a program to clear a list in Python
list = ['Mon', 'Tue', 'Wed', 'Thu']
print("Existing list\n",list)
#clear the list
list.clear()
print("After clearing the list\n")
print(list)

#Q-8 write a program to Reversing a List

# Reversing a list using reversed()
def Reverse(lst):
    return [ele for ele in reversed(lst)]
     
# Driver Code
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

#Q-9 write a program to find sum of elements in list
total = 0
# creating a list
list1 =[1,2,3,4,5]
for ele in range(0, len(list1)):
   total = total + list1[ele]
# main
print("Sum of all elements in given list: ", total)

#Q-10 write a program to Multiply all numbers in the list
# Python program to multiply all values in the
# list using traversal
 
def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result
     
# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))