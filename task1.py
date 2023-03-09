##  1)write a program to print fibonacci series upto the given number

# Give input of desired range
num = 60

# Initialize first two numbers
a, b = 0, 1

# Create an empty list o store the o/p
op = [0, 1]

# Write the condition
while a + b <= num:
    op.append(a + b)
    a, b = b, a + b
print("Fibonacci Series up to", num, ":", op)


print("#####or######")

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b

num = int(input("Enter a number: "))

print("Fibonacci series up to", num, ":")
fibonacci(num)