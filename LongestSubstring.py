def lengthOfLongestSubstring(s: str) -> int:
    stack = []
    highestcount = 0

    for i in range(len(s)):
        if s[i] in stack:
            highestcount = max(len(stack), highestcount)
            stack = stack[stack.index(s[i]) + 1:]
        stack.append(s[i])

    return max(len(stack), highestcount)


string = input("Enter a string: ")
print("Length of the longest substring without repeating characters:", lengthOfLongestSubstring(string))