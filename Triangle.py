
a = int(input('Enter the first side of the triangle:'))
b = int(input('Enter the second side of the triangle:'))
c = int(input('Enter the third side of the triangle:'))

if a<b+c and b<c+a and c<a+b:
    result ="The size of each side is smaller than the sum of the size of the other two sides."
else:
    result="The size of each side is not smaller than the sum of the size of the other two sides."
print(result)
