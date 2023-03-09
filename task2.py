## 2)write a program to print the lists which contain numbers divisible by 3, divisibly by 5 and divisible by 3 and 5 and print each in a separate list.
## l = [3, 5, 2, 11, 15, 30, 45, 9, 12, 20]


l = [3, 5, 2, 11, 15, 30, 45, 9, 12, 20]

# Creating empty lists to store the o/p's
divisible_by_3 = []
divisible_by_5 = []
divisible_by_3_and_5 = []

# condition to perform
for i in l:
	if i % 3 == 0 and i % 5 == 0:  # using modular division to check which are divisible by 3 & 5 who's remainder is zero.
		divisible_by_3_and_5.append(i)  # and inserting into the empty list
	elif i % 3 == 0:   # to perform another condition to check which are divisible by 3
		divisible_by_3.append(i)  # and inserting into the empty list
	elif i % 5 == 0:  # to perform another condition to check which are divisible by 5
		divisible_by_5.append(i)  # and inserting into the empty list


print("divisible_by_3:", divisible_by_3)  # to see the resultant o/p
print("divisible_by_5:", divisible_by_5)  # to see the resultant o/p
print("divisible_by_3_and_5:", divisible_by_3_and_5)   # to see the resultant o/p