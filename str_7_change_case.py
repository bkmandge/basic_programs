str1 = input("Enter the string: ")

while True:
    print("1. Upper 2. Lower 3.Swapcase 4. Title 5.Quit")
    n = int(input("Select the operation: "))

    if n == 1:
        print(str1.upper())
    elif n == 2:
        print(str1.lower())
    elif n == 3:
        print(str1.swapcase())
    elif n == 4:
        print(str1.title())
    elif n == 5:
        break
    else:
        print("Select the correct operation!")
