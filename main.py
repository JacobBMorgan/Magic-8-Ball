import random

def switch_table(argument):
    switcher = {
        1: "It is certain.",
        2: "It is decidedly so.",
        3: "Without a doubt.",
        4: "Yes, definitely.",
        5: "You may rely on it.",
        6: "As I see it, yes.",
        7: "Most likely.",
        8: "Outlook good.",
        9: "Yes.",
        10: "Signs point to yes.",
        11: "Reply hazy, try again.",
        12: "Ask again later.",
        13: "Better not tell you now.",
        14: "Cannot predict now.",
        15: "Concentrate and ask again.",
        16: "Don't count on it.",
        17: "My reply is no.",
        18: "My sources say no.",
        19: "Outlook not so good.",
        20: "Very doubtful."
    }
    return switcher.get(argument, 'Invalid entry')

while True:
    dieRoll = random.randint(1, 20)
    input("What wisdom do you seek from me? ")
    print(switch_table(dieRoll), "\n")

    while True:
        playAgain = input("Do you seek further wisdom? Yes or no? ")
        if playAgain == "yes":
            break

        elif playAgain == "no":
            print("Return to me when you seek further wisdom.")
            exit()

        else:
            print("It's a yes or no question. Try again.")