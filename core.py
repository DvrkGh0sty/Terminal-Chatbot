class Calculations():
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        while True:        
            try:
                result = num1/num2
            except ZeroDivisionError:
                print('Error cannot divide by zero')
                return None
        return result
