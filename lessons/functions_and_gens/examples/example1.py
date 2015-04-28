num = 10
print id(num)

def square_x(x): #arguments are aka parameters
    x *= x
    return x

print square_x(num)
print(num)
print(id(num))