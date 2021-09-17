points: int = 0
player: str = ""

def main() -> None:
    greet()
    direction: str = input("Would you like to play the hard version, easy version, or quit? Please type 1 for the hard version, 2 for the easy version, and 3 to quit.")
    if (direction == "1"):
        hardversion()
    elif (direction == "2"):
        easyversion()
    else:
        end()

def greet() -> None:
    player = input("Enter Player Name: ")
    print(player + ", Welcome to ____! Please answer the following questions to the best of your ability and we will tell you how big of a F.R.I.E.N.D.S fan you are!")

def hardversion() -> None:

def easyversion() -> None: 

def end() -> None:
    print(f"Thank you for playing. Congratulations on gaining {points} Adventure points")

__name__: str = "__main__"
if __name__ == "__main__":
    main()