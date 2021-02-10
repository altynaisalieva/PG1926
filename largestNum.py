
def maxNum (arr,n):
    max=arr[0];
    for i in range (1,n):
        if (arr[i]>max):
            max=arr[i];
    return max           


if __name__ == "__main__" : 
      
    arr = [];
    number=int(input("Enter number of elements: "))
for i in range(0,number):
     arr1=int(input("Enter num to array: "))
     arr.append(arr1) 
     
     n = len(arr);
print(arr)
maxn=maxNum(arr,n)
print("Largest in given array is ", maxn)
