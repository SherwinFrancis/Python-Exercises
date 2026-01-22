def lengthOfLastWord(s) :
        s = s.split(' ')
        for i in range(len(s) - 1,-1,-1):
            if s[i] != ' ' and s[i] != "":
                return len(s[i])