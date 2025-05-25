# Implement strStr()*
def strStr(haystack, needle):
    if needle == "":
        return 0
    if needle in haystack:
        return haystack.index(needle)
    return -1

# Test cases*
print(strStr("hello", "ll"))     # Output: 2
print(strStr("aaaaa", "bba"))    # Output: -1
