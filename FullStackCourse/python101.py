import random
while True:
    myanswer = input("Choose: rock, paper or scissors:")
    myanswer = myanswer.lower()

    if myanswer=="quit":
        print("Exit")

    if myanswer !='rock' and myanswer!='paper' and myanswer !='scissors':
        print("Please choose a valid answer")
        continue
    computer_answer = random.choice(["rock","paper","scissors"])
    print(f"Computer chose: {computer_answer}")

    if myanswer == computer_answer:
        print("Tie !")
        continue
    elif myanswer =="paper" and computer_answer=="rock":
        print("You win !")
        break
    elif myanswer =="rock" and computer_answer=="paper":
        print("You win!")
        break
    else:
        print("You lose!")
        continue