from core import Calculations
from core import teach
from core import get_response
from core import game
calc = Calculations()
def main():
    print('Welcome to the terminal chatbot.')
    print('Use /programs to access extra programs.')
    print('/exit to exit the program')
    while True:
        user_input = input('> ').strip()

        if user_input.lower() in ['/program', '/programs']:
            print('1. Calculate (Basic features)')
            print('2. Teach & Learn')
            print('3. Load Data')
            print('4. Game')

            try:
                option = int(input('Choose 1-4: '))
            except ValueError:
                print('Please enter a number (1 or 2).')
                continue

            # --- Calculator ---
            if option == 1:
                choice = input('Add, Subtract, Divide or Multiply: ').lower()

                try:
                    num1 = float(input('Num1: '))
                    num2 = float(input('Num2: '))

                    if choice == 'add':
                        result = calc.add(num1, num2)
                    elif choice == 'subtract':
                        result = calc.subtract(num1, num2)
                    elif choice == 'multiply':
                        result = calc.multiply(num1, num2)
                    elif choice == 'divide':
                        result = calc.divide(num1, num2)
                    else:
                        print('Invalid operation.')
                        continue

                except ValueError:
                    print('Please enter valid numbers.')
                    continue
                except ZeroDivisionError:
                    print('Cannot divide by zero.')
                    continue

                print(f'Answer: {result}')
                continue

            # --- Teach & Learn ---
            elif option == 2:
                print('Teach & Learn: teach me phrases and responses.')
                word_or_phrase = input('Enter keyword: ').strip()
                user_reply = input('Enter response: ').strip()

                if word_or_phrase and user_reply:
                    saved_data = teach(word_or_phrase, user_reply)
                    print(f'Data has been saved. Expected response: {saved_data}')
                else:
                    print('Keyword and response cannot be empty.')

            # ---Load Data ---
            elif option == 3:
                try:
                    with open("test.txt", "r") as fs:
                        lines = fs.readlines()

                    if not lines:
                        print("No saved data found.")
                    else:
                        for i, line in enumerate(lines, start=1):
                            print(f"{i}. {line.strip()}")

                except FileNotFoundError:
                    print("No saved data file found yet.")

                    
            elif option == 4:
                num_of_round = int(input("How many rounds would you like to play: "))
                guess = input('What is your choice: ')
                games = game(num_of_round,)

        elif user_input in ['/exit', '/quit']:
            print('Thank you for chat.')
            break
        else:
            reply = get_response(user_input)
            print(reply)

if __name__ == '__main__':
    main()


