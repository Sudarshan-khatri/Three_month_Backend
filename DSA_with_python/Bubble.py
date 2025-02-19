"""Bubble sort is the simplest algorithm that work by repeatedly swapping the adjacent element
if they are in wrong order

pseudo code:
Bubblesort(A,n)
for i in range(n-1):
    for j in range(n-i-1):
        if(A[j]>A[j+1]):
            temp=A[j]
            A[j]=A[j+1]     //pythonic way :A[j],A[j+1]=A[j+1],A[j]
            A[j+1]=temp

time complexity:
  worst case:O(n^2)
  Best case:O(1)

Advantages 
 *Bubble sort is easy to understand and implement 
 *It is a stable algorithm
Disadvantages
 *Bubble sort has time complexity of O(n^2)which makes it is very slow for large dataset
 *Bubble sort has almost no or limited real world applications
      
"""


 




list=[]
num=int(input("Input the size of list:"))
for i in range(num):
    value=int(input("Enter the number:"))
    list.append(value)
print(f"original list:{list}")

for i in range(0,num-1):
    for j in range(0,num-i-1):
        if(list[j]>list[j+1]):
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print(f"list after sorting:{list}")