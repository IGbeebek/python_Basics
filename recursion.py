# Write a recursive function to calculate the sum of first n natural numbers.
def calc_Sum(n):
    if(n == 0):
        return 0
    return calc_Sum(n-1) + n
sum = calc_Sum(5)
print(sum)

# Write a recursive function to print all elements in a list. (use list and index as parameters).
def print_List(list, index = 0):
    if(index == len(list)):
        return
    print(list[index])
    print_List(list, index + 1)

fruits = ["Apple", "Orange", "Banana", "Grapes"]
print_List(fruits)