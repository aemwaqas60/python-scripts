def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


number = int(input('Please enter a number to calculate the factorial : '))
print(f'Factorial of {number} :  {factorial(number)}')
