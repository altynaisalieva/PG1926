def printArr(arr, n) :  
  
    for i in range(n) :

     
        print(arr[i],end=" ")  
       
def reorder(arr, n) :  
  
    count1 = 0
       
    for i in range(n) : 
        if (arr[i] != 1) : 
            arr[count1] = arr[i] 
            count1 += 1
  
    while (count1 < n) : 
        arr[count1] = 1
        count1 += 1
   
    lastNonOne = 0
    for i in range(n - 1, -1, -1) : 
  
      
        if (arr[i] == 1) :  
            continue
              
        if (not lastNonOne) : 
  
           
            lastNonOne = i 
  
       
        if (arr[i] != 0) : 
            arr[lastNonOne] = arr[i] 
            lastNonOne -= 1
   
    while (lastNonOne >= 0) : 
        arr[lastNonOne] = 0
        lastNonOne -= 1
if __name__ == "__main__" : 
      
    arr = [];
    number=int(input("Enter number of elements: "))
for i in range(0,number):
     arr1=int(input("Enter num to array: "))
     arr.append(arr1) 
     
     n = len(arr);
print(arr)
reorder(arr, n)  
printArr(arr, n) 
  
