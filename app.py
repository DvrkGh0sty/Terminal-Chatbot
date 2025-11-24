from core import Calculations
from core import teach
from core import get_response
calc = Calculations()
def main():
    print('Welcome to the terminal chatbot.')
    print('Use /programs to access extra programs.')

    while True:
        user_input = input('> ').strip()

        if user_input.lower() in ['/program', '/programs']:
            print('1. Calculate (Basic features)')
            print('2. Teach & Learn')

            try:
                option = int(input('Choose 1-2: '))
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
                    continue
        else:
            pass
            #placeholder for actual chat

if __name__ == '__main__':
    main()
