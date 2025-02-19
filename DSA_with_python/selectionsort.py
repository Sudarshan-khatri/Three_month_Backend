"""
Selection sort is a comparison based sorting algorithm.It sort an array by repeatedly selecting
the smallest(or largest )element from the unsorted array and swapping it with the first unsorted
element . This process continue untill the entire array is sorted

Pseudo code
SelectionSort(A,n)
 {
   for(i=0;i<n;i++)
    {
      least=A[i]
      p=i
      for(j=i+1;j<n;J++)
       {
        if(A[j]<least)
         {
           least=A[j]
           p=j
         }
       }
       swap(A[j],A[p])
    }
 }
Advantages:
  It is easier to implement and understand 
  Require only a constant O(1) extra memeory space
  It require less number of swap compared to other algorithms 
DIsadvantages:
  Selection sort has time complexity of O(n^2)make it slower compared to other algorithms
  It is not stable algorithms
"""

def selectionSort(A,n):
    for i in range(n):
        least=A[i]
        p=i
        for j in range(i+1,n):
            if(A[j]<least):
                least=A[j]
                p=j
            
        A[i],A[p]=A[p],A[i]

    print(f"List after sorting:{A}")

if __name__ == "__main__":
  
    list=[]
    num=int(input("Enter the size of list:"))
    
    #append the number to selection sort in list
    for i in range(num):
        value=int(input("Number for sort:"))
        list.append(value)

    print(f"original list:{list}")

    selectionSort(list,num)

