def longestCommonPrefix(strs):
        common = ""
        strs = sorted(strs,key=len)
        for i in range(0, len(strs[0])):
            for word in strs:
                if word[i] != strs[0][i]:
                    return common 

            common += strs[0][i]
        return common

