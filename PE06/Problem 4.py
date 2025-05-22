#Remove Duplicates from Sorted Array*
def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    i = 0  #track unique values*
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i = i + 1
            nums[i] = nums[j]
    return i + 1 

nums = [0,0,1,1,1,2,2,3,3,4]
length = remove_duplicates(nums)
print("New length:", length)
print("Updated array:", nums[:length])

