welcome = "Welcome to the Quiz Game!"
print(welcome)

instructions = "\nThis  quiz contains 5 questions that you need to answer\n\nYou will have 30 seconds to answer each question\n"
print(instructions)

playing = input("\nAre you ready to play the game? (Y/N) \n")
if playing != "Y":
    quit()

questions = [
    "What is the Roman name of the Greek god Zeus?",
    "What is the Latin word for the liquid produced by the Ficus Elastica?",
    "What won an Emmy for outstanding music direction in 1985?",
    "When did the 'Eighty Years War' start?",
    "The English explorer Admiral John Franklin discovered what in the 1840s?",
]

answers = [
    "Jupiter",
    "Latex",
    "Christmas In Washington",
    "1568",
    "The Northwest Passage",
]

correct = 0
incorrect = 0
gotCorrect = []
gotWrong = []
userInputs = []

index = 0

while index < len(questions):
    print(f"\n{questions[index]}")
    userInput = input("Enter your response: ")
    if userInput == answers[index]:
        correct += 1
        gotCorrect.append(questions[index])
    else:
        incorrect += 1
        userInputs.append(answers[index])
        gotWrong.append(questions[index])
    index += 1


print(f"✅ correct:  {correct}\n❌ incorrect: {incorrect}\n")
check = input("Would you like to view what you got correct and wrong? (Y/N) \n")
if check == "Y":
    if gotCorrect and gotWrong:
        for right in gotCorrect:
            print(
                f"{right} - ✅ correct\n",
            )
        for wrong in gotWrong:
            print(f"{wrong} - ❌ incorrect\n")
        quit()
    elif gotCorrect:
        for right in gotCorrect:
            print(f"{right} - correct\n")
        quit()
    else:
        for wrong in gotWrong:
            print(f"{wrong} - incorrect\n")
            for input in userInputs:
                print(input)
    quit()
