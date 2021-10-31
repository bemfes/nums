nums = list(map(int, input('Введите числа: ').split()))
def is_monotonic(nums):
    isAscending = True
    isDescending = True
    for i in range(1,len(nums)):
        if(nums[i] >= nums[i-1]):
            isDescending = False
        elif(nums[i] <= nums[i-1]):
            isAscending = False
        if((not isAscending) and (not isDescending)):
            print("False")
            break
    if(isAscending):
        print("True")
    if(isDescending):
        print("True")
is_monotonic(nums)
