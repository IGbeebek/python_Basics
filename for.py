# Print numbers from 1 to 100.
for i in range(1,101):
    print(i)

# Print numbers 100 to 1.
for i in range(100, 0, -1):
    print(i)

# Print the multiplication table of a number n.
n = int(input("Enter the value of n: "))
for i in range(1,11):
    print(n * i)

# WAP to find the factorial of first n numbers.
n = int(input("Enter the value of n:"))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial value: ",fact)