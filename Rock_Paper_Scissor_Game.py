
import random
choices = ["Rock","Paper","Scissor"]
print("Choices:")
print("1. Rock")
print("2. Paper")
print("3. Scissor")
print("4. Quit")
user_count = 0
computer_count = 0
tie_count = 0
while True:
    user_choice = input("Enter your choice: ")
    if user_choice == "Quit":
        print("GoodBye!")
        break

    computer_choice = random.choice(choices)
    print(f"\nUser choice: {user_choice} \nComputer Choice: {computer_choice}")

    if user_choice == computer_choice:
        tie_count = tie_count + 1
        print("It's a tie match")
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        user_count = user_count + 1
        print("You won!")
    else:
        computer_count = computer_count + 1
        print("Computer wons!")    

print(f"User Win: {user_count}")
print(f"Computer Win: {computer_count}")
print(f"Tie : {tie_count}")
