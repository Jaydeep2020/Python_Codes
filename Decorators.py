def divide(a,b):
    return a/b
    
def decorator(func):
    def wrapper(a,b):
        if b==0:
            a,b = b,a
        return func(a,b)
    return wrapper
    

a, b = 10,0

deco = decorator(divide)
ans = deco(a,b)
print(ans)
