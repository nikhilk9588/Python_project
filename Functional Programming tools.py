# Functional Programming tools

print('#######(1) filter #########')

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even(a):
	if a % 2 == 0:
		return a

print(filter(even, l))  #0x000001866978B760 represents the speed of iteration
print(list(filter(even, l)))


print('#########(2) map ##########')

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def mul(b):
	#if b % 2 ==0:
	return b * 2

print(map(mul, l1))
print(list(map(mul, l1)))

print('#######(3) reduce #########')

from functools import reduce

def add(a, b):
	#print((a, b), a + b)
	return a + b

r = [1, 2, 3, 4, 5]
print(reduce(add, r))

print('#######(4) zip #########')

l2 = [1, 2, 3]
l3 = [4, 5, 6]
l4 = [7, 8, 9]

print(list(zip(l2, l3, l4)))
print(dict(zip(l2, l3)))
print(list(zip('hello', 'world', 'python')))


print('####### to get combinations in the given data structure #########')

from itertools import combinations

combs = combinations([3, 5, 6, 7, 2, 9, 8], 2)
print(list(combs))


print('####### to get combinations in the given data structure by using a condition #########')

from itertools import combinations

combs = combinations([3, 5, 6, 7, 2, 9, 8], 2)
print([i for i in combs if sum(i) == 11])

# lambda functions
print("###### lambda functions #####")

add = lambda a,b,c, : a + b + c

print(add(10, 20, 30))


print("##### lambda functions with functional programming tools")

l5 = [1, 2, 3, 4, 5]

print(list(map(lambda a : a ** 3, l5)))

print(list(filter(lambda a : a % 2 == 0, l5)))