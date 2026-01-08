def product_fib(_prod):
    a = 0
    b = 1
    
    if _prod == 0:
        return [0,1,True]
    
    while a * b < _prod:
        
        old_a = a 
        a = b 
        b = old_a + b
        
        if a * b == _prod:
            return [a,b,True]
        elif a * b > _prod:
            return [a,b, False]
        
print(product_fib(161710837))