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
    print('The questions are based on these categories: \n')

    for category in categories:
        print(category)
    print()


# Displays the questions the user can choose between, user chooses inputs the number they want.
def displayQuestions():
    print('Choose a question: \n')
    print('Geography:')
    print('1. What is the capital of Sweden?')
    print('2. What is the largest river in South America?')
    print('Music:')
    print("3. Who had a 1984 hit with 'I Want to Know What Love Is?")
    print("4. Which trio of brothers released the song 'Mmm Bop’ in 1997?")
    print('General Knowledge:')
    print('5. What is the chemical symbol for gold?')
    print('6. Which country hosted the 2016 Summer Olympics?')


# Ask user for input.
# the if statement in this code is borrowed from Jimmy's adventure game.
def fetchUserInput():
    ans = input('Answer: ')
    print()
    if ans.isdigit():
        if int(ans) >= 1 and int(ans) <7:
            return int(ans)
    print()


categories1 = ['❀ Geography', '❀ Music', '❀ General Knowledge']


# Main program
welcomeScreen()
displayCategories(categories1)
userName()

# Main loop/game loop
run = True
while run:

    # startGame()
    displayQuestions()
    choice = fetchUserInput()

    choice = int(choice)
    if choice == 1:
        print('What is the capital of Sweden?')
        answer = input('Answer: ')
        print()
        if answer == 'Stockholm' or answer == 'stockholm' or answer == 'STOCKHOLM':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')

    elif choice == 2:
        print('What is the largest river in South America?')
        answer = input('Answer: ')
        print()
        if answer == 'Amazon' or answer == 'amazon' or answer == 'AMAZON':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')

    elif choice == 3:
        print("Who had a 1984 hit with 'I Want to Know What Love Is'?")
        answer = input('Answer: ')
        print()
        if answer == 'Foreigner' or answer == 'foreigner' or answer == 'FOREIGNER':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')

    elif choice == 4:
        print("Which trio of brothers released the song 'Mmm Bop’ in 1997?")
        answer = input('Answer: ')
        print()
        if answer == 'Hanson' or answer == 'hanson' or answer == 'HANSON':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')

    elif choice == 5:
        print('What is the chemical symbol for gold?')
        answer = input('Answer: ')
        print()
        if answer == 'Au' or answer == 'au' or answer == 'AU':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')

    elif choice == 6:
        print('Which country hosted the 2016 Summer Olympics?')
        answer = input('Answer: ')
        print()
        if answer == 'Brazil' or answer == 'brazil' or answer == 'BRAZIL':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')

    else:
        print('Sorry, I cannot understand what you want to do.')

displayQuestions()
