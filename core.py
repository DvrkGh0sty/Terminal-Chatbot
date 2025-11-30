import random
class Calculations():
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            print('Error cannot divide by zero')
            return None

data = {
    
}

def teach(keyword, reply):
    data[keyword] = reply
    with open('test.txt', 'a') as log:
        log.write(f'\n{keyword}: {reply}')
    return reply

def get_response(prompt):
    responses = {
    'hi': 'Hello There, I am X-bot, your terminal chatbot, designed to help you in your journy (in Beta rn)',
    'bye': 'Thank you, goodbye'
    }
    if prompt in responses:
        return responses[prompt]
    else:
        print('Sorry, as we are still in beta I cannot answer your question')

def game(rounds):
    ai_score = 0
    user_score = 0

    parts = ['rock', 'paper', 'scissor']

    for _ in range(rounds):

        user_guess = input("Rock, Paper, or Scissor: ").strip().lower()
        cpu_choice = random.choice(parts)

        print(f"CPU chose: {cpu_choice}")

        # USER LOSES
        if user_guess == 'rock' and cpu_choice == 'paper':
            print('CPU wins, +1 point!')
            if user_score > 0:
                user_score -= 1
            ai_score += 1

        elif user_guess == 'paper' and cpu_choice == 'scissor':
            print('CPU wins, +1 point!')
            if user_score > 0:
                user_score -= 1
            ai_score += 1

        elif user_guess == 'scissor' and cpu_choice == 'rock':
            print('CPU wins, +1 point!')
            if user_score > 0:
                user_score -= 1
            ai_score += 1

        # USER WINS
        elif user_guess == 'paper' and cpu_choice == 'rock':
            print('You win, +1 point')
            if ai_score > 0:
                ai_score -= 1
            user_score += 1

        elif user_guess == 'rock' and cpu_choice == 'scissor':
            print('You win, +1 point')
            if ai_score > 0:
                ai_score -= 1
            user_score += 1

        elif user_guess == 'scissor' and cpu_choice == 'paper':
            print('You win, +1 point')
            if ai_score > 0:
                ai_score -= 1
            user_score += 1

        # TIE
        elif user_guess == cpu_choice:
            print('TIE, no points awarded')

        else:
            print("Invalid choice. Try again.")
            continue

        print(f"Score → You: {user_score} | AI: {ai_score}\n")

    return f'Final Score:\nYou: {user_score}\nAI: {ai_score}'


def vigenere_encrypt_file(input_file, output_file, key):
    key = key.lower().strip()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""

    # Read the original file
    with open(input_file, "r") as f:
        data = f.read()

    key_index = 0
    key_length = len(key)

    for char in data:
        if char.lower() in alphabet:
            # Position of the text character
            char_index = alphabet.index(char.lower())

            # Position of the key character (repeated)
            key_char = key[key_index % key_length]
            key_shift = alphabet.index(key_char)

            # Encrypt: (text + key) mod 26
            new_index = (char_index + key_shift) % 26
            new_char = alphabet[new_index]

            # Preserve uppercase/lowercase
            encrypted_text += new_char.upper() if char.isupper() else new_char

            key_index += 1   # Advance key only for letters
        else:
            # Keep punctuation, numbers, spaces, etc.
            encrypted_text += char

    # Write encrypted result to a new file
    with open(output_file, "w") as f:
        f.write(encrypted_text)

    return f"Encrypted file saved as: {output_file}"

def generate_password(length):
    passwd = ''
    count = 0
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890#!@$%*&^+_-'
    for char in range(0, length):
        char = random.choice(chars)
        passwd += char
        count += 1
    return passwd
