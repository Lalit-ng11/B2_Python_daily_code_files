# Array / List 
arr= [] 

arr.append(50)
arr.append(20)
arr.append(10)
arr.append(30)
arr.append(60) 
print("The OG array/List =",arr)
# o/p = The OG array/List = [50, 20, 10, 30, 60]

# print("element at index number 2 =",arr[2])
# o/p = element at index number 2 = 10 
# arr[3]=40
# print("Updated Arr =",arr)
#o/p = Updated Arr = [50, 20, 10, 40, 60]

# arr.remove(20)
# print("Updated Arr =",arr)
# Updated Arr = [50, 10, 40, 60] 

# elements = 20 
# if elements in arr :
#     print("The element is present in arr.")
# else: 
#     print("The element is Absent in arr.")
    
# o/p = The element is present in arr.

# Bubble sort Algorithm 
# arr = [50, 20, 10, 30, 60] 
n = len(arr) 
for i in range(0,n):
    for j in range(i+1 ,n): 
        if arr[i] > arr[j]: 
            arr[i],arr[j] = arr[j],arr[i] 
print("After Sorting =",arr)
'''
The OG array/List = [50, 20, 10, 30, 60]
After Sorting = [10, 20, 30, 50, 60]
'''










