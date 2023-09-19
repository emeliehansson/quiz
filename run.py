# Displays the welcome screen to the user.
def welcomeScreen():
    print("Welcome to Emelie's quiz!!")
    print('❁❁❁❁❁❁❁❁❁❁❁❁❁❁❁❁❁')
    print('Are you ready? Good Luck!')
    print()


# Asks the user for their name, username or what they want to give.
def userName():
    # Ask for username
    print('Please give me your name: ')
    name = input('Name: ')
    print()
    # Prints a hello string with the users name
    print(f'Hello, {name}')
    print()


def displayCategories(categories):
    print('You can choose from the following categories:\n')

    for category in categories:
        print(category)
    print()


# Displays the questions the user can choose between, user chooses inputs the number they want.
def displayQuestions():
    print('Choose a question: \n')
    print('1. What is the capital of Sweden?')
    print("2. Which female artist sings the song 'Rolling in the deep'?")
    print('3. How many days in year?')
    print('4. Pepsi or Coca Cola?')


# Ask user for input.
# the if statement in this code is borrowed from Jimmy's adventure game.
def fetchUserInput():
    ans = input('Answer: ')
    print()
    if ans.isdigit():
        if int(ans) >= 1 and int(ans) <5:
            return int(ans)
    print()


categories1 = ['Geography', 'Music', 'General Knowledge']

# Main program

welcomeScreen()
userName()

# Main loop/game loop
run = True
while run:

    # startGame()
    displayCategories(categories1)
    displayQuestions()
    choice = fetchUserInput()

    choice = int(choice)
    if choice == 1:
        print('What is the capital of Sweden?')
        answer = input('Answer: ')
        print()
        if answer == 'Stockholm' or answer == 'stockholm':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')

    elif choice == 2:
        print("Which female artist sings the song 'Rolling in the deep'?")
        answer = input('Answer: ')
        if answer == 'Adele':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')

    elif choice == 3:
        print("How many days in year'?")
        answer = input('Answer: ')
        print()
        if answer == str(365):
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')

    elif choice == 4:
        print('Pepsi or Coca Cola?')
        answer = input('Answer: ')
        print()
        if answer == 'Pepsi' or answer == 'pepsi':
            print(f"☆ That's correct! {answer} always wins! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( Pepsi is always the winner! \n')

    else:
        print('Sorry, I cannot understand what you want to do.')

displayQuestions()
