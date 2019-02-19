
first_number = int(input("""
    Please enter a number:
    """))
operator = input("""
    Please enter a math operator:
    """)
second_number = int(input("""
    Please enter a second number:
    """))

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        print(f"""
    The answer is {a + b}
    """)

    def subtract(self, a, b):
        print(f"""
    The answer is {a - b}
    """)

    def multiply(self, a, b):
        print(f"""
    The answer is {a * b}
    """)

    def divide(self, a, b):
        print(f"""
    The answer is {a / b}
    """)

calculator = Calculator()

if operator == '-':
    calculator.subtract(first_number, second_number)
elif operator == '+':
    calculator.add(first_number, second_number)
elif operator == '*':
    calculator.multiply(first_number, second_number)
elif operator == '/':
    calculator.divide(first_number, second_number)
else:
    print("error")
