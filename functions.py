# WAF to print the length of a list. (List is the parameter)
cities = ["Kathmandu", "Chitwan", "Itahari", "Damak"]
num = [1,2,3,4,5,6,7,8]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(num)

# WAF to print the elements of a list in a single line. (List is the parameter)
def print_List(list):
    for item in list:
        print(item, end = " ")

print_List(cities)

# WAF to find the factorial of n. (n is the parameter)
def cal_Fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_Fact(5)

# WAF to convert USD to NPR.
def converter(usd_Val):
    npr_Val = usd_Val * 147.68
    print(usd_Val, "USD:", npr_Val, "NPR")
converter(5)