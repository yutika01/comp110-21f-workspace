from random import randint

points: int = 0
player: str = ""
round: int = 1
win_emoji: str = "\U0001F973"
clover: str = "\U0001F340"
fail: str = "\U0001F61F"

def main() -> None:
    greet()
    direction: str = input("Would you like to play the hard version, easy version, or quit? Please type 1 for the hard version, 2 for the easy version, and 3 to quit: ")
    global round
    global points
    while round > 0:
        if (direction == "1"):
            hardversion()
        elif (direction == "2"):
            points = easyversion(points)
        else:
            end()
        print(f"Total points: {points}")
        if (input("Do you want to play again? Type 'YES' or 'NO' ")) == "YES":
            main()
        else: 
            end()

def greet() -> None:
    global player
    global clover
    player = input("Enter Player Name: ")
    print(f"{player}, Welcome to Friends Trivia! Please answer the following questions to the best of your ability and we will tell you how big of a F.R.I.E.N.D.S fan you are!")
    print(f"Enter the correct answer to get points. Good luck! {clover}")

def hardversion() -> None:
    print(f"Welcome {player}! Let's begin.")
    global points
    q1: str = input("What is the name of the restaurant Monica was head chef at? ")
    if q1 == "Alessandro's":
        points = points + 1
        print(f"Current points: {points}")
    q2: str = input("What book did Chandler buy for Kathy? ")
    if q2 == "The Velveteen Rabbit":
        points = points + 1
        print(f"Current points: {points}")
    q3: str = input("Where did Pheobe's love interest, David, go to work? ")
    if q3 == "Minsk":
        points = points + 1
        print(f"Current points: {points}")
    print("Finally, a bonus question! This question is worth 2 points.")
    randgen()
    
def easyversion(points_easy: int) -> int: 
    global player
    print(f"Welcome {player}! Let's begin.")
    q1: str = input("How many times was Ross divorced? ")
    if q1 == "3":
        points_easy += 1
        print(f"Current points: {points_easy}")
    else: print("Incorrect")
    q2: str = input("What was the incorrect ingredient in Rachel's thanksgiving trifle? ")
    if q2 == "Beef with peas and onions":
        points_easy += 1
        print(f"Current points: {points_easy}")
    else: print("Incorrect")
    q3: str = input("Who had a crush on Joshua? ")
    if q3 == "Rachel":
        points_easy += 1
        print(f"Current points: {points_easy}")
    return points_easy

def end() -> None:
    global round
    global win_emoji
    global fail
    round = round - 1
    print(f"Thank you for playing. Congratulations on gaining {points} Adventure points!")
    if points >= 2:
        print(f"You are a true fan! {win_emoji}")
    elif points >= 1: 
        print("You are a fan, but need to brush up on your knowledge")
    elif points < 1:
        print(f"Uh oh! You may need to rewatch F.R.I.E.N.D.S {fail}")

def randgen() -> None:
    global points
    num = randint(1,4)
    if num == 1:
        rand_question: str = input("What does Rachel think Chandler's job is? ")
        if rand_question == "A transponster":
            points += 2
            print(f"Current points: {points}")
    elif num == 2:        
        rand_question2: str = input("What is the name of Ross's pet monkey? ")
        if rand_question2 == "Marcel":
            points += 2
            print(f"Current points: {points}")
    elif num == 3:
        rand_question3: str = input("Pheobe finds what in her soda can? ")
        if rand_question3 == "A human thumb":
            points += 2
            print(f"Current points: {points}")
    else: 
        rand_question4: str = input("Who was Monica's first kiss? ")
        if rand_question4 == "Ross":
            points += 2
            print(f"Current points: {points}")

__name__: str = "__main__"
if __name__ == "__main__":
    main()