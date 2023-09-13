# Welcome screen
print('Are you ready to quiz? Good Luck!')
print('---------------------------------')

# Main loop/game loop
run = True
while run:
    # Ask for username
    print('Please give me your name: ')
    name = input('Name: ')
    print(f'Hello {name}')
    print()

    # Ask for user input
    print('So... Are you ready?')
    print('1. For sure!')
    print("2. Don't think so..")
    print('Make a choice by pressing A or B \n')

    # User input
    choice = input('Answer: ')
    print()
    # Sanitize user input
    if not choice.isnumeric():
        print('Please provide an answer')

    # Ask for user input
    choice = int(choice)
    if choice == 1:
        print('Here we go!! \n')
    elif choice == 2:
        print('That is really sad..')
        print('Bye bye')
        run = False
    else:
        print("That's not an option, I hope you're ready then.. \n")

    # Ask for user input if user wants to play with multiple choice (easier) or not.
    print('Do you want to play with multiple choice or not? (yes/no)')
    choice = input('Answer: ')
    print()

    # Questions with multiple choice
    if choice == 'yes' or choice == 'Yes':
        print('Choose a question: \n')
        print('1. What country drinks the most coffee per capita?')
        print('2. What city is known as "The Eternal City"?')
        print('3. What is the highest-rated film on IMDb as of September 1st, 2023?')
        print('4. How many bones do we have in an ear?')
        print('5. Random question')

        # User input
        choice = input('Answer: ')
        print()

        choice = int(choice)
        if choice == 1:
            print('What country drinks the most coffee per capita?')
            print('''
                1. Sweden
                2. Italy
                3. Finland
                4. Portugal
            \n''')
            answer = input('Answer: ')
            if answer == 'Finland' or answer == 'finland' or answer == str(3):
                print(f"{answer} is correct! Great job! \n")
            else:
                print('Sorry, wrong answer.. :( \n')

        if choice == 2:
            print('What city is known as "The Eternal City"?')
            print('''
                1. Rome
                2. Barcelona
                3. Amsterdam
                4. Berlin
            \n''')
            answer = input('Answer: ')
            if answer == 'Adele' or answer == 'adele' or answer == str(1):
                print(f"{answer} is correct! Great job! \n")
            else:
                print('Sorry, wrong answer.. :( \n')

        if choice == 3:
            print("What is the highest-rated film on IMDb as of September 1st, 2023?")
            print('''
                1. The Lord of the Rings: The Return of the King
                2. The Godfather
                3. Pulp Fiction
                4. The Shawshank Redemption
            \n''')
            answer = input('Answer: ')
            if answer == 'The Shawshank Redemption' or answer == 'the shawshank redemption' or answer == str(4):
                print(f"{answer} is correct! Great job! \n")
            else:
                print('Sorry, wrong answer.. :( \n')

        if choice == 4:
            print('How many bones do we have in an ear?')
            print('''
                1. Seven
                2. Three
                3. Four
                4. Six
            \n''')
            answer = input('Answer: ')
            if answer == 'Three' or answer == 'three' or answer == str(2):
                print(f"{answer} is correct! Great job! \n")
            else:
                print('Sorry, wrong answer.. :( \n')
        continue

    # Quiz without multiple choice, the user has to write out the answer
    if choice == 'no' or choice == 'No':
        # Quiz questions
        print('Choose a question: \n')
        print('1. What is the capital of Sweden?')
        print("2. Which female artist sings the song 'Rolling in the deep'?")
        print('3. How many days in year?')
        print('4. Pepsi or Coca Cola?')

        # User input
        choice = input('Answer: ')
        print()

        choice = int(choice)
        if choice == 1:
            print('What is the capital of Sweden?')
            answer = input('Answer: ')
            if answer == 'Stockholm' or answer == 'stockholm':
                print(f"{answer} is correct! Great job! \n")
            else:
                print('Sorry, wrong answer.. :( \n')

        if choice == 2:
            print("Which female artist sings the song 'Rolling in the deep'?")
            answer = input('Answer: ')
            if answer == 'Adele':
                print(f"{answer} is correct! Great job! \n")
            else:
                print('Sorry, wrong answer.. :( \n')

        if choice == 3:
            print("How many days in year'?")
            answer = input('Answer: ')
            if answer == str(365):
                print(f"{answer} is correct! Great job! \n")
            else:
                print('Sorry, wrong answer.. :( \n')

        if choice == 4:
            print('Pepsi or Coca Cola?')
            answer = input('Answer: ')
            if answer == 'Pepsi':
                print(f"That's correct! {answer} always wins! \n")
            else:
                print('Sorry, wrong answer.. :( Pepsi is always the winner! \n')
        continue



