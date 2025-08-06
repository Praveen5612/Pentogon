class Calculation:
    def calculate(self, a, b):
        Addition = a + b
        Subtraction = a - b
        Multiplication = a * b
        Division = a / b      
        return {
            'Addition': Addition,
            'Subtraction': Subtraction,
            'Multiplication': Multiplication,
            'Division': Division
        }   
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
calc = Calculation()
print(calc.calculate(a, b))