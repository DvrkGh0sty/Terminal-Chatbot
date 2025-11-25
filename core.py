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

def load_data(saved_data):
    with open('test.txt', 'r') as sd:
        for sentence in sd:
            print(f'Here is your loaded data: {sentence} ')
        return sentence
