#This Python program reads a sorted list of integers, including negative numbers, squares each number, 
# and returns a new list with the squares in sorted (non-decreasing) order — without using any built-in sorting functions.
def sorted_squares(arr):
    n=len(arr)
    result=[0]*5
    left=0
    right=n-1
    pos=n-1
    while left<=right:
        sq_left=arr[left]**2
        sq_right=arr[right]**2
        if sq_left > sq_right:
            result[pos]=sq_left
            left+=1
        else:
            result[pos]=sq_right
            right-=1
        pos-=1
    return result
nums=list(map(int,input().split()))
result=sorted_squares(nums)
print(result)

