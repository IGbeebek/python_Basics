# Print numbers from 1 to 100
numbers = 1
while numbers <= 100:
    print(numbers)
    numbers += 1

# print numbers from 100 to 1
num = 100
while num >= 1:
    print(num)
    num -= 1

# Print the multiplication table of a number n.
n = int(input("Enter the value of n: "))
i = 1
while i <= 10:
    print(i * n)
    i += 1

# Print the elements of the following list using loop.
# [1,4,9,16,25,36,49,64,81,100]
list1 = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

# Search for a number x in this using loop.
# (1,4,9,16,25,36,49,64,81,100)
Tuple1 = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0
while i < len(Tuple1):
    if(Tuple1[i] == x):
        print("Found at index: ", i)
        break
    else:
        print("Finding..")
    i += 1
print("End of loop.")

# WAP to find the sum of first n numbers.
n = int(input("Enter the value of n: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Total sum:", sum)
