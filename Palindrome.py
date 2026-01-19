def isPalindrome(x: int) -> bool:
    strX = str(x)
    if strX[::-1] == strX:
        return True 
    else:
        return False
        
        