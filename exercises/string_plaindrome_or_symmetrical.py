string = "malayalam"


def isSymmetricalOrPalindrome(string):
    half = int(len(string) / 2)

    firstHalf = string[:half]
    secondHalf = string[half:]

    if firstHalf == secondHalf:
        print(f"The string {string}  is symmetrical")
    else:
        print(f"The string {string} is not symmetrical")

    if string == string[::-1]:
        print(f'The string {string} is palindrome')
    else:
        print(f'The string {string} is not palindrome')


while True:
    myString = input("Please enter the string to check it is palindrome or  symmetrical : ")
    isSymmetricalOrPalindrome(myString)
    userInput = input(f"Please type add for new input or exit.")
    if userInput == 'exit':
        break
print(f'Bye...')
