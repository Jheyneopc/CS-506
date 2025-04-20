#Valid Anagram*
def isAnagram(s, t):
    return sorted(s) == sorted(t)

# Test cases*
print(isAnagram("anagram", "nagaram"))  # Output: True
print(isAnagram("rat", "car"))          # Output: False
