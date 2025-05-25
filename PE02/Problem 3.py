#Longest Common Prefi*
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

# Test cases*
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
