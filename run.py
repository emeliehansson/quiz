import time


# Displays the welcome screen to the user.
def welcomeScreen():
    print("Welcome to Emelie's quiz!!")
    print('❁❁❁❁❁❁❁❁❁❁❁❁❁❁❁❁❁❁')
    print('Are you ready? Good Luck!')
    print()


# Asks for input for the user to provide their name, username or what they want to give.
# The output prints a string that welcomes the user by using their name, ex: "Hello, Emelie".
def userName():
    # Ask for username
    print('Please give me your name: ')
    name = input('Name: ')
    print()
    # Prints a hello string with the users name
    print(f'Hello, {name}')
    print()
    time.sleep(1)


# Displays the categories with a for loop
def displayCategories(categories):
    print('The questions are based on these categories: \n')

    for category in categories:
        print(category)
    print()


# Displays the questions, user chooses by pressing the number they want.
# Option of quitting game is also available here.
def displayQuestions():
    print('Choose an option: \n')
    print('Press a number from 1-6 or press 0 to quit the game.')
    print('Geography:')
    print('1. What is the capital of Sweden?')
    print('2. What is the largest river in South America?')
    print('Music:')
    print("3. Who had a 1984 hit with 'I Want to Know What Love Is?")
    print("4. Which trio of brothers released the song 'Mmm Bop’ in 1997?")
    print('General Knowledge:')
    print('5. What is the chemical symbol for gold?')
    print('6. Which country hosted the 2016 Summer Olympics?')
    print('0. Press 0 to quit game.')


# Asks user for input of the questions.
# The if statement in this code is borrowed from Jimmy's adventure game.
def fetchUserInput():
    ans = input('Answer: ')
    print()
    if ans.isdigit():
        if int(ans) >= 0 and int(ans) < 7:
            return int(ans)
    print()


# This list displays the categories, used in displayCategories function.
categories1 = ['❀ Geography', '❀ Music', '❀ General Knowledge']


# Main program, shows welcome screen, categories and asks for username.
welcomeScreen()
displayCategories(categories1)
userName()

# Main loop/game loop
run = True
while run:

    # Starts the game by displaying questions and asking user for input.
    displayQuestions()
    choice = fetchUserInput()

    # If statement to handle input that is not accepted in the game.
    if choice == -1:
        print('Sorry! I did not understand what you meant? Please give me a number.')
        continue

    # If/else statements for choices of the questions.
    # The number chosen will display the question and then ask for input.
    # The option to quit game available.
    if choice == 1:
        print('What is the capital of Sweden?')
        answer = input('Answer: ')
        print()
        if answer == 'Stockholm' or answer == 'stockholm' or answer == 'STOCKHOLM':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')
        time.sleep(1.5)

    elif choice == 2:
        print('What is the largest river in South America?')
        answer = input('Answer: ')
        print()
        if answer == 'Amazon' or answer == 'amazon' or answer == 'AMAZON':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')
        time.sleep(1.5)

    elif choice == 3:
        print("Who had a 1984 hit with 'I Want to Know What Love Is'?")
        answer = input('Answer: ')
        print()
        if answer == 'Foreigner' or answer == 'foreigner' or answer == 'FOREIGNER':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')
        time.sleep(1.5)

    elif choice == 4:
        print("Which trio of brothers released the song 'Mmm Bop’ in 1997?")
        answer = input('Answer: ')
        print()
        if answer == 'Hanson' or answer == 'hanson' or answer == 'HANSON':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')
        time.sleep(1.5)

    elif choice == 5:
        print('What is the chemical symbol for gold?')
        answer = input('Answer: ')
        print()
        if answer == 'Au' or answer == 'au' or answer == 'AU':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')
        time.sleep(1.5)

    elif choice == 6:
        print('Which country hosted the 2016 Summer Olympics?')
        answer = input('Answer: ')
        print()
        if answer == 'Brazil' or answer == 'brazil' or answer == 'BRAZIL':
            print(f"☆ {answer} is correct! Great job! ☆ \n")
        else:
            print('Sorry, wrong answer.. :( \n')
        time.sleep(1.5)
        displayQuestions()

    elif choice == 0:
        print('Do you want to quit game? y/n')
        answer = input('Answer: ')
        print()
        if answer == 'y' or answer == 'Y':
            print('Sorry to see you go.. bye bye')
            time.sleep(1)
            run = False
            # welcomeScreen()
        elif answer == 'n' or answer == 'N':
            print("Let's keep going!")
            time.sleep(0.5)
    else:
        print('Sorry, I cannot understand what you want to do.')


# Displays the questions again after the user has given an answer.
# displayQuestions()
