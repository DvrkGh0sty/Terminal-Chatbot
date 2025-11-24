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

response = {
    'Hello': 'Hi There',
    'Exit': 'Goodbye'
}

def teach(keyword, reply):
    response[keyword] = reply
    with open('data.txt', 'a') as log:
        log.write(f'\n{keyword}: {reply}')
    return reply



