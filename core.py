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
