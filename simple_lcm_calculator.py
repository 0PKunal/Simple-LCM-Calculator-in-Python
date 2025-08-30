#function for lcm calculation
def lcm(a, b):
    maxNum = max(a, b)
    while True: 
        if maxNum % a == 0 and maxNum % b == 0:
            return maxNum
        maxNum += 1

#custom range
x = int(input(f'\nNumber of Set\'s: '))

#loop for multipale set's
for i in range(1, x+1):
    print(f'\nSet no. {i}:')
    num1 = int(input("Enter the First number: "))
    num2 = int(input("Enter the Second number: "))
    print(f'\nThe lcm of {num1} and {num2} is {lcm(num1, num2)}')
