import random

yourName = "[YOUR NAME HERE]"
yourSouthHillsUserName = "[YOUR USERNAME HERE]"

print(f"Hello, {yourName} | {yourSouthHillsUserName}")

verificationNum = random.randint(1, 99)

try:
    userNumber = int(input(f"Enter the number {verificationNum} in your terminal: "))

    if (verificationNum == userNumber):
        print("Great! You're done with this lab.")
    else:
        print("Please run the program again and enter the correct input.")
except Exception as e:
    print("Error!")
    print(e)