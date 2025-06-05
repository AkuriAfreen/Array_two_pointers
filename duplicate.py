nums=list(map(int,input().split()))
duplicates=[]
if len(set(nums))==len(nums):
    print("null")
else:
    for num in nums:
        if nums.count(num)>1 and num not in duplicates:
            duplicates.append(num)
    print("duplicates:",duplicates)