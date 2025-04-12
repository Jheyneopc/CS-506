#Check if N and its double exist*
def check_if_double_exists(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == 2 * arr[j]:
                return True
    return False

print("Check [10,2,5,3]:", check_if_double_exists([10,2,5,3]))
print("Check [3,1,7,11]:", check_if_double_exists([3,1,7,11]))
