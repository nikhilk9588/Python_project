#Functions

#write a program to get the last element.

l = [1, 2, 3, 4, 5]

def get_last_element(l):   #called functiom
	return l[-1]

print(get_last_element(l))  #calling function

print(get_last_element([0, 1, 2, 3]))  #calling function

print(get_last_element([-1, -2, -3, -4])) #calling function


#write a program to accept 3 values and return the sum of values.

def add(x, y, z):
	return sum([x, y, z])  #or x + y + z

print(add(10, 20, 30))
print(add(1, 2, 3))


def mul(a, b = 0, c = 0):
	print(a, b, c)
	return a * b * c

print(mul(1, 2, 3))
print(mul(5, 6, 7))