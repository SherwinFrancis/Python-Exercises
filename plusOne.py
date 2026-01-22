def plusOne(digits):
        string = ""
        for i in range(0, len(digits)):
            string += str(digits[i])
        string = str(int(string) + 1)
        newlist = []
        for i in range(0,len(string)):
            newlist.append(int(string[i]))
        return newlist