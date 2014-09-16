
# Our real numbers will default to float.
x = 1.1
y = 2.2

print("x, %s, %17f") % (type(x), x)
print("y, %s, %17f") % (type(y), y)

#Ok, everything looks good... now add them together to get 3.3
z = x + y

print("z, %s: %.15f at 15 decimals") % (type(z), z)
print("z, %s: %.17f at 17 decimals") % (type(z), z)
print("z, %s: %.33f at 33 decimals") % (type(z), z)
print("Oh no!")
