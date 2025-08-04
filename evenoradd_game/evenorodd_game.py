import random
options = ["even", "odd"]
user_input = int(input("Enter your number: "))
guess = int(input("Guess 'even' or 'odd' and enter 0 for even or 1 for odd: "))
com_choice = random.randint(0, 100)
print(f"Computer choice is {com_choice}")
sum = com_choice+user_input
if sum%2==guess:
    print("You win!")
else:
    print("You lose!")