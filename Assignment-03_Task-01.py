#Calculate Factorial Using a Function
q =int(input('Enter a number: '))
def fact(a):
    if a==0:
        return 1
    else:
        return a * fact(a-1)
print('Factorial of',q,'is',fact(q))
